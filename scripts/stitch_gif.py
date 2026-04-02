#!/usr/bin/env python3
"""
Stitch PNG frames into an animated GIF using Pillow.

Usage:
  python3 scripts/stitch_gif.py [--fps 15] [--scale 0.5]

Reads frames from art/output/gif_frames/, outputs to art/output/india_breathes_2025.gif
"""

import argparse
import glob
import os
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FRAMES_DIR = ROOT / "art" / "output" / "gif_frames"
OUT_GIF = ROOT / "art" / "output" / "india_breathes_2025.gif"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fps", type=int, default=15, help="Frames per second")
    parser.add_argument("--scale", type=float, default=0.6, help="Scale factor (1.0 = full size)")
    args = parser.parse_args()

    frame_paths = sorted(glob.glob(str(FRAMES_DIR / "frame_*.png")))
    if not frame_paths:
        print(f"No frames found in {FRAMES_DIR}")
        return

    print(f"Loading {len(frame_paths)} frames...")
    duration_ms = int(1000 / args.fps)

    frames = []
    for i, fp in enumerate(frame_paths):
        img = Image.open(fp).convert("RGB")
        if args.scale != 1.0:
            new_size = (int(img.width * args.scale), int(img.height * args.scale))
            img = img.resize(new_size, Image.LANCZOS)
        frames.append(img)
        if i % 50 == 0:
            print(f"  Loaded {i + 1}/{len(frame_paths)}")

    print(f"Saving GIF ({frames[0].width}x{frames[0].height}, {args.fps} fps, {len(frames)} frames)...")
    frames[0].save(
        OUT_GIF,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
    )

    size_mb = os.path.getsize(OUT_GIF) / (1024 * 1024)
    print(f"Saved: {OUT_GIF} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
