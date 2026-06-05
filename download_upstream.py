"""Helper script to download and extract upstream fonts for Yeomil Mono builder.

Downloads Geist Mono and Pretendard CJK zip archives and extracts them to upstream/.
"""

import logging
import urllib.request
import zipfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

GEIST_URL = "https://github.com/vercel/geist-font/releases/download/v1.7.2/geist-font-v1.7.2.zip"
PRETENDARD_URL = (
    "https://github.com/orioncactus/pretendard/releases/download/v1.3.9/Pretendard-1.3.9.zip"
)


def download_and_extract(url: str, dest_dir: Path, zip_filename: str) -> None:
    """Download zip from url and extract it into dest_dir."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    zip_path = dest_dir / zip_filename

    if not zip_path.exists():
        logger.info("Downloading %s to %s...", url, zip_path)
        # Add User-Agent header to avoid potential blocks
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})  # noqa: S310
        with urllib.request.urlopen(req) as response, zip_path.open("wb") as f:  # noqa: S310
            f.write(response.read())
        logger.info("Download completed.")
    else:
        logger.info("Zip file already exists: %s. Skipping download.", zip_path)

    logger.info("Extracting %s to %s...", zip_path, dest_dir)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dest_dir)
    logger.info("Extraction completed.")

    # Remove temporary zip file
    zip_path.unlink()


def main() -> None:
    """Download upstream resources."""
    upstream_dir = Path("upstream")
    try:
        download_and_extract(GEIST_URL, upstream_dir / "geist-font", "geist-font.zip")
        download_and_extract(PRETENDARD_URL, upstream_dir / "pretendard", "pretendard.zip")
        logger.info("All upstream resources downloaded and prepared successfully!")
    except Exception as e:
        logger.exception("Failed to prepare upstream resources")
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()
