"""Yeomil Mono font builder module.

Handles merging Geist Mono and Pretendard CJK fonts with strict monospace alignment.
"""

import logging
from pathlib import Path
from typing import Any, cast

from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

logger = logging.getLogger(__name__)


def is_cjk(code: int) -> bool:
    """Determine if a Unicode codepoint belongs to the CJK/Hangul ranges."""
    return (
        # Hangul Syllables
        (0xAC00 <= code <= 0xD7A3)
        # Hangul Jamo
        or (0x1100 <= code <= 0x11FF)
        # Hangul Compatibility Jamo
        or (0x3130 <= code <= 0x318F)
        # Hangul Jamo Extended-A/B
        or (0xA960 <= code <= 0xA97F or 0xD7B0 <= code <= 0xD7FF)
        # CJK Unified Ideographs (Hanja)
        or (0x4E00 <= code <= 0x9FFF)
        # CJK symbols & punctuation, fullwidth forms, etc.
        or (0x3000 <= code <= 0x303F)
        or (65280 <= code <= 65519)
    )


def update_font_names(font: TTFont, family_name: str, subfamily_name: str) -> None:
    """Update font family, subfamily, and PostScript names in the name table."""
    logger.info("Updating font names to %s %s...", family_name, subfamily_name)
    name_table = font["name"]

    ps_family = family_name.replace(" ", "")
    ps_subfamily = subfamily_name.replace(" ", "")
    ps_name = f"{ps_family}-{ps_subfamily}"
    full_name = f"{family_name} {subfamily_name}"
    head_table = cast("Any", font["head"])
    unique_id = f"{ps_name};{head_table.fontRevision:.3f}"

    for record in name_table.names:
        name_id = record.nameID
        try:
            encoding = record.getEncoding()
            if name_id == 1:  # Font Family
                record.string = family_name.encode(encoding)
            elif name_id == 2:  # Font Subfamily
                record.string = subfamily_name.encode(encoding)
            elif name_id == 3:  # Unique Identifier
                record.string = unique_id.encode(encoding)
            elif name_id == 4:  # Full Font Name
                record.string = full_name.encode(encoding)
            elif name_id == 6:  # PostScript Name
                record.string = ps_name.encode(encoding)
            elif name_id == 16:  # Typographic Family Name
                record.string = family_name.encode(encoding)
            elif name_id == 17:  # Typographic Subfamily Name
                record.string = subfamily_name.encode(encoding)
        except Exception as e:  # noqa: BLE001
            logger.warning("Failed to update name record %d: %s", name_id, e)


def merge_fonts(  # noqa: PLR0912, PLR0913, PLR0915, C901
    latin_path: str,
    cjk_path: str,
    output_path: str,
    family_name: str,
    subfamily_name: str,
    cjk_scale: float = 1.0,
) -> None:
    """Merge Latin font with CJK font and align metrics for terminal usage.

    Ensures CJK glyphs are centered horizontally and given exactly 2x Latin advance width.
    """
    logger.info("Merging: %s + %s -> %s", latin_path, cjk_path, output_path)

    # Load fonts
    latin_font = TTFont(latin_path)
    cjk_font = TTFont(cjk_path)

    latin_head = cast("Any", latin_font["head"])
    cjk_head = cast("Any", cjk_font["head"])
    latin_upm = latin_head.unitsPerEm
    cjk_upm = cjk_head.unitsPerEm

    # Calculate scale factor to match UPM and apply custom visual scaling
    upm_scale = latin_upm / cjk_upm
    total_scale = upm_scale * cjk_scale

    logger.info(
        "UPMs: Latin=%d, CJK=%d. Total scaling factor=%.6f", latin_upm, cjk_upm, total_scale
    )

    latin_cmap = latin_font.getBestCmap()
    cjk_cmap = cjk_font.getBestCmap()

    if not latin_cmap or not cjk_cmap:
        msg = "Fonts must have valid cmap tables"
        raise ValueError(msg)

    latin_font.getGlyphSet()
    cjk_glyph_set = cjk_font.getGlyphSet()

    glyf_table = latin_font["glyf"]
    hmtx_table = latin_font["hmtx"]

    # We expect Latin width to be exactly 600, CJK target width to be exactly 1200
    target_cjk_width = 1200

    # Map Hangul Jamo to Hangul Compatibility Jamo
    choseong_map = {
        0x1100: 0x3131,
        0x1101: 0x3132,
        0x1102: 0x3134,
        0x1103: 0x3137,
        0x1104: 0x3138,
        0x1105: 0x3139,
        0x1106: 0x3141,
        0x1107: 0x3142,
        0x1108: 0x3143,
        0x1109: 0x3145,
        0x110A: 0x3146,
        0x110B: 0x3147,
        0x110C: 0x3148,
        0x110D: 0x3149,
        0x110E: 0x314A,
        0x110F: 0x314B,
        0x1110: 0x314C,
        0x1111: 0x314D,
        0x1112: 0x314E,
    }
    jungseong_map = {code: 0x314F + (code - 0x1161) for code in range(0x1161, 0x1175 + 1)}
    jongseong_map = {
        0x11A8: 0x3131,
        0x11A9: 0x3132,
        0x11AA: 0x3133,
        0x11AB: 0x3134,
        0x11AC: 0x3135,
        0x11AD: 0x3136,
        0x11AE: 0x3137,
        0x11AF: 0x3139,
        0x11B0: 0x313A,
        0x11B1: 0x313B,
        0x11B2: 0x313C,
        0x11B3: 0x313D,
        0x11B4: 0x313E,
        0x11B5: 0x313F,
        0x11B6: 0x3140,
        0x11B7: 0x3141,
        0x11B8: 0x3142,
        0x11B9: 0x3144,
        0x11BA: 0x3145,
        0x11BB: 0x3146,
        0x11BC: 0x3147,
        0x11BD: 0x3148,
        0x11BE: 0x314A,
        0x11BF: 0x314B,
        0x11C0: 0x314C,
        0x11C1: 0x314D,
        0x11C2: 0x314E,
    }
    all_jamo_map = {}
    all_jamo_map.update(choseong_map)
    all_jamo_map.update(jungseong_map)
    all_jamo_map.update(jongseong_map)

    # Collect codepoints to merge
    cjk_codepoints = [code for code in cjk_cmap if is_cjk(code)]
    # Ensure all Jamo codepoints are included in cjk_codepoints for processing
    for jamo_code in all_jamo_map:
        if jamo_code not in cjk_codepoints:
            cjk_codepoints.append(jamo_code)

    logger.info("Found %d CJK codepoints (including Jamos) to merge.", len(cjk_codepoints))

    # Add new glyphs
    glyph_order = latin_font.getGlyphOrder()

    copied_count = 0
    for code in cjk_codepoints:
        # Determine source glyph name in CJK font
        if code in all_jamo_map:
            comp_code = all_jamo_map[code]
            if comp_code in cjk_cmap:
                cjk_glyph_name = cjk_cmap[comp_code]
            else:
                logger.warning("Compatibility Jamo 0x%04X not found in CJK cmap", comp_code)
                continue
        else:
            cjk_glyph_name = cjk_cmap[code]

        if cjk_glyph_name not in cjk_glyph_set:
            continue

        target_glyph_name = f"uni{code:04X}"

        # Calculate bounding box of source glyph to center it
        bounds_pen = BoundsPen(cjk_glyph_set)
        cjk_glyph_set[cjk_glyph_name].draw(bounds_pen)

        if bounds_pen.bounds is not None:
            xmin, _ymin, xmax, _ymax = bounds_pen.bounds
            scaled_xmin = xmin * total_scale
            scaled_xmax = xmax * total_scale

            # Center the glyph horizontally in the 1200 unit box
            current_center = (scaled_xmin + scaled_xmax) / 2
            target_center = target_cjk_width / 2
            shift_x = target_center - current_center

            new_lsb = round(scaled_xmin + shift_x)
        else:
            shift_x = 0
            new_lsb = 0

        # Draw and fully flatten all components using DecomposingRecordingPen
        dec_pen = DecomposingRecordingPen(cjk_glyph_set)
        cjk_glyph_set[cjk_glyph_name].draw(dec_pen)

        # Draw decomposed paths to TTGlyphPen with scaling and shifting
        pen = TTGlyphPen(None)
        tpen = TransformPen(pen, (total_scale, 0, 0, total_scale, shift_x, 0))
        dec_pen.replay(tpen)

        # Inject glyph and update metrics
        new_glyph = pen.glyph()
        glyf_table[target_glyph_name] = new_glyph
        hmtx_table.metrics[target_glyph_name] = (target_cjk_width, new_lsb)

        # Update cmap in all subtables
        for table in latin_font["cmap"].tables:
            table.cmap[code] = target_glyph_name

        if target_glyph_name not in glyph_order:
            glyph_order.append(target_glyph_name)

        copied_count += 1

    logger.info("Copied and centered %d CJK glyphs.", copied_count)

    # Update glyph order in font
    latin_font.setGlyphOrder(glyph_order)

    # Update OS/2 table flags for CJK/Hangul unicode ranges
    logger.info("Copying Unicode/Codepage ranges from Pretendard...")
    for field in [
        "ulUnicodeRange1",
        "ulUnicodeRange2",
        "ulUnicodeRange3",
        "ulUnicodeRange4",
        "ulCodePageRange1",
        "ulCodePageRange2",
    ]:
        setattr(latin_font["OS/2"], field, getattr(cjk_font["OS/2"], field))

    # Enforce strict Monospace flags
    logger.info("Enforcing strict Monospace flags...")
    post_table = cast("Any", latin_font["post"])
    post_table.isFixedPitch = 1
    os2_table = cast("Any", latin_font["OS/2"])
    os2_table.panose.bProportion = 9

    # Compile and add GSUB ccmp features for NFD support
    logger.info("Generating and compiling GSUB ccmp features for NFD support...")
    fea_lines = [
        "languagesystem DFLT dflt;",
        "languagesystem latn dflt;",
        "languagesystem hang dflt;",
        "",
        "feature ccmp {",
    ]

    choseong_list = sorted(choseong_map.keys())
    jungseong_list = sorted(jungseong_map.keys())
    jongseong_list = sorted(jongseong_map.keys())

    # 3-Jamo substitutions
    for c_idx, c_code in enumerate(choseong_list):
        for v_idx, v_code in enumerate(jungseong_list):
            for t_idx, t_code in enumerate(jongseong_list):
                syllable_code = 0xAC00 + (c_idx * 21 * 28) + (v_idx * 28) + (t_idx + 1)
                fea_lines.append(
                    f"    sub uni{c_code:04X} uni{v_code:04X} "
                    f"uni{t_code:04X} by uni{syllable_code:04X};"
                )

    # 2-Jamo substitutions
    for c_idx, c_code in enumerate(choseong_list):
        for v_idx, v_code in enumerate(jungseong_list):
            syllable_code = 0xAC00 + (c_idx * 21 * 28) + (v_idx * 28)
            fea_lines.append(f"    sub uni{c_code:04X} uni{v_code:04X} by uni{syllable_code:04X};")

    fea_lines.append("} ccmp;")
    fea_content = "\n".join(fea_lines)

    try:
        addOpenTypeFeaturesFromString(latin_font, fea_content)
        logger.info("GSUB ccmp features successfully added.")
    except Exception:
        logger.exception("Failed to add GSUB ccmp features")
        raise

    # Update names
    update_font_names(latin_font, family_name, subfamily_name)

    # Create output dir if needed
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Save merged font
    logger.info("Saving merged font to %s...", output_path)
    latin_font.save(output_path)
    logger.info("Successfully saved merged font.")
