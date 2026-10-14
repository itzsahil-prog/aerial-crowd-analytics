"""
Download a free aerial crowd sample video from Pexels.

Usage:
    python assets/download_sample.py

Saves to: assets/sample_aerial.mp4

The video is "Aerial View of Crowded Outdoor Gathering" from Pexels (free to use,
no attribution required under the Pexels License).
Pexels page: https://www.pexels.com/video/aerial-view-of-crowded-outdoor-gathering-36410760/
"""

import os
import sys
import urllib.request

# Direct HD download URL for Pexels video #36410760
# (1280x720, ~10s, aerial top-down crowd — best for this app)
VIDEO_URL = (
    "https://videos.pexels.com/video-files/36410760/"
    "36410760-uhd_2560_1440_24fps.mp4"
)
FALLBACK_URL = (
    "https://videos.pexels.com/video-files/3941289/"
    "3941289-hd_1920_1080_30fps.mp4"
)

OUT_DIR = os.path.join(os.path.dirname(__file__))
OUT_PATH = os.path.join(OUT_DIR, "sample_aerial.mp4")


def _progress(block_num, block_size, total_size):
    if total_size > 0:
        pct = min(100, block_num * block_size * 100 // total_size)
        bar = "█" * (pct // 5) + "░" * (20 - pct // 5)
        print(f"\r  [{bar}] {pct}%", end="", flush=True)


def download(url, dest):
    print(f"Downloading from:\n  {url}")
    print(f"Saving to: {dest}\n")
    try:
        urllib.request.urlretrieve(url, dest, reporthook=_progress)
        print("\nDone.")
        return True
    except Exception as e:
        print(f"\nFailed: {e}")
        return False


if __name__ == "__main__":
    if os.path.exists(OUT_PATH):
        size_mb = os.path.getsize(OUT_PATH) / 1_000_000
        print(f"Sample already exists ({size_mb:.1f} MB): {OUT_PATH}")
        sys.exit(0)

    os.makedirs(OUT_DIR, exist_ok=True)

    if not download(VIDEO_URL, OUT_PATH):
        print("Trying fallback video...")
        if not download(FALLBACK_URL, OUT_PATH):
            print("\nBoth downloads failed.")
            print("Please download manually from:")
            print("  https://www.pexels.com/video/aerial-view-of-crowded-outdoor-gathering-36410760/")
            sys.exit(1)

    size_mb = os.path.getsize(OUT_PATH) / 1_000_000
    print(f"\nSaved: {OUT_PATH} ({size_mb:.1f} MB)")
    print("\nTo use in the app:")
    print("  1. Run: streamlit run app.py")
    print("  2. In the sidebar, select 'Upload video'")
    print("  3. Upload assets/sample_aerial.mp4")
