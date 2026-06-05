"""Yeomil Mono command-line interface.

Allows running the font builder with custom arguments.
"""

import argparse
import logging
import sys
from pathlib import Path

from fontTools.ttLib import TTFont

from yeomil_mono.builder import merge_fonts

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for yeomil-mono."""
    parser = argparse.ArgumentParser(
        description="Merge Geist Mono and Pretendard CJK into a perfectly aligned monospace font."
    )
    parser.add_argument(
        "--latin-dir",
        default="upstream/geist-font/geist-font/GeistMono/ttf",
        help="Directory containing Geist Mono TTF files.",
    )
    parser.add_argument(
        "--cjk-dir",
        default="upstream/pretendard/public/static/alternative",
        help="Directory containing Pretendard TTF files.",
    )
    parser.add_argument(
        "--output-dir",
        default="fonts",
        help="Directory to save the merged fonts.",
    )
    parser.add_argument(
        "--family-name",
        default="Yeomil Mono",
        help="Name of the merged font family (default: Yeomil Mono).",
    )
    parser.add_argument(
        "--scale", type=float, default=1.0, help="Scale factor for the CJK glyphs (default: 1.0)."
    )
    parser.add_argument(
        "--weights",
        nargs="+",
        default=["Regular", "Bold", "Light"],
        help="Weights to generate (default: Regular Bold Light).",
    )

    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    logger.info("Starting Yeomil Mono build...")

    latin_dir = Path(args.latin_dir)
    cjk_dir = Path(args.cjk_dir)

    # Establish subdirectories (Unified Font Repository v0.3)
    base_output_dir = Path(args.output_dir)
    ttf_dir = base_output_dir / "ttf"
    otf_dir = base_output_dir / "otf"
    web_dir = base_output_dir / "webfont"

    ttf_dir.mkdir(parents=True, exist_ok=True)
    otf_dir.mkdir(parents=True, exist_ok=True)
    web_dir.mkdir(parents=True, exist_ok=True)

    for weight in args.weights:
        # Check files exist
        latin_filename = f"GeistMono-{weight}.ttf"
        cjk_filename = f"Pretendard-{weight}.ttf"

        latin_path = latin_dir / latin_filename
        cjk_path = cjk_dir / cjk_filename

        output_filename_ttf = f"{args.family_name.replace(' ', '')}-{weight}.ttf"
        output_filename_otf = f"{args.family_name.replace(' ', '')}-{weight}.otf"
        output_filename_woff2 = f"{args.family_name.replace(' ', '')}-{weight}.woff2"

        output_path_ttf = ttf_dir / output_filename_ttf
        output_path_otf = otf_dir / output_filename_otf
        output_path_woff2 = web_dir / output_filename_woff2

        if not latin_path.exists():
            logger.error("Latin font file not found: %s", latin_path)
            return 1
        if not cjk_path.exists():
            logger.error("CJK font file not found: %s", cjk_path)
            return 1

        try:
            # 1. Compile TTF
            merge_fonts(
                latin_path=str(latin_path),
                cjk_path=str(cjk_path),
                output_path=str(output_path_ttf),
                family_name=args.family_name,
                subfamily_name=weight,
                cjk_scale=args.scale,
            )

            # 2. Compile OTF (OpenType wrapper of merged TTF structure)
            logger.info("Saving OpenType OTF: %s", output_path_otf)
            font_obj = TTFont(str(output_path_ttf))
            font_obj.save(str(output_path_otf))

            # 3. Compile WOFF2
            logger.info("Converting to WOFF2: %s", output_path_woff2)
            font = TTFont(str(output_path_ttf))
            font.flavor = "woff2"
            font.save(str(output_path_woff2))
        except Exception:
            logger.exception("Failed to build weight %s", weight)
            return 1

    # 4. Write web font CSS mapping file
    write_css(web_dir, args.family_name, args.weights)

    logger.info("All requested weights built successfully!")
    return 0


def write_css(output_web_dir: Path, family_name: str, weights: list[str]) -> None:
    """Generate @font-face rules for compiled web fonts."""
    css_content = []
    weight_map = {
        "Thin": 100,
        "ExtraLight": 200,
        "Light": 300,
        "Regular": 400,
        "Medium": 500,
        "SemiBold": 600,
        "Bold": 700,
        "ExtraBold": 800,
        "Black": 900,
    }
    for weight in weights:
        num_weight = weight_map.get(weight, 400)
        font_filename = f"{family_name.replace(' ', '')}-{weight}.woff2"
        css_content.append(
            f"@font-face {{\n"
            f"  font-family: '{family_name}';\n"
            f"  src: url('./{font_filename}') format('woff2');\n"
            f"  font-weight: {num_weight};\n"
            f"  font-style: normal;\n"
            f"  font-display: swap;\n"
            f"}}\n"
        )
    css_filename = f"{family_name.replace(' ', '').lower()}.css"
    css_path = output_web_dir / css_filename
    css_path.write_text("\n".join(css_content), encoding="utf-8")
    logger.info("Wrote web font CSS to %s", css_path)


if __name__ == "__main__":
    sys.exit(main())
