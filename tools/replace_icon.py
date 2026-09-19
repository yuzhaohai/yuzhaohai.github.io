#!/usr/bin/env python3
"""Replace all favicons + avatar with a single source image (center-cropped to square)."""
from PIL import Image
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "assets/img/sample/new-icon.png")
FAV = os.path.join(BASE, "assets/img/favicons")
AVATAR_OUT = os.path.join(BASE, "assets/img/sample/avatar.png")

# 1. Open and center-crop to square
img = Image.open(SRC).convert("RGBA")
w, h = img.size
side = min(w, h)
left = (w - side) // 2
top = (h - side) // 2
square = img.crop((left, top, left + side, top + side))
print(f"source {w}x{h} -> square {side}x{side}")

# 2. All PNG sizes referenced by the theme
sizes = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "favicon-96x96.png": 96,
    "apple-icon.png": 180,
    "apple-icon-precomposed.png": 180,
    "apple-icon-57x57.png": 57,
    "apple-icon-60x60.png": 60,
    "apple-icon-72x72.png": 72,
    "apple-icon-76x76.png": 76,
    "apple-icon-114x114.png": 114,
    "apple-icon-120x120.png": 120,
    "apple-icon-144x144.png": 144,
    "apple-icon-152x152.png": 152,
    "apple-icon-180x180.png": 180,
    "android-icon-36x36.png": 36,
    "android-icon-48x48.png": 48,
    "android-icon-72x72.png": 72,
    "android-icon-96x96.png": 96,
    "android-icon-144x144.png": 144,
    "android-icon-192x192.png": 192,
    "ms-icon-70x70.png": 70,
    "ms-icon-144x144.png": 144,
    "ms-icon-150x150.png": 150,
    "ms-icon-310x310.png": 310,
}
for name, s in sizes.items():
    out = os.path.join(FAV, name)
    square.resize((s, s), Image.LANCZOS).save(out, "PNG")
    print(f"  wrote {name} ({s}x{s})")

# 3. favicon.ico with multiple sizes
ico = os.path.join(FAV, "favicon.ico")
square.resize((64, 64), Image.LANCZOS).save(
    ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)]
)
print(f"  wrote favicon.ico (16/32/48)")

# 4. Avatar (square, 400px is plenty for the sidebar)
square.resize((400, 400), Image.LANCZOS).save(AVATAR_OUT, "PNG")
print(f"  wrote avatar.png (400x400)")

print("done")
