"""Rebuild logo variants and favicons from logo/logo.png (requires Pillow)."""
from pathlib import Path

from PIL import Image, ImageOps

root = Path(__file__).resolve().parents[1]
(root / 'favicon').mkdir(exist_ok=True)
with Image.open(root / 'logo/logo.png') as source:
    logo = source.convert('RGBA')
logo.save(root / 'logo/logo.webp', 'WEBP', lossless=True)
square = ImageOps.pad(logo, (716, 716), color=(0, 0, 0, 0))
for size in (32, 192):
    square.resize((size, size), Image.Resampling.LANCZOS).save(
        root / f'favicon/favicon-{size}.png'
    )
square.resize((256, 256), Image.Resampling.LANCZOS).save(
    root / 'favicon/favicon.ico',
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)
