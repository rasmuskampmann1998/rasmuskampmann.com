"""
Render 1600x900 cover for the TomatoIntel case study.

The existing JPG (835x422) is a light-mode dashboard screenshot with right-side
whitespace. We crop the whitespace, upscale the result to a tight 16:9 size,
center it on a #0A0A0A canvas, and add a lime-green frame plus a caption.
"""
from __future__ import annotations

import os
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(SITE_ROOT, "assets", "images", "projects", "tomato-intel.jpg")
OUT = os.path.join(SITE_ROOT, "assets", "images", "projects", "tomato-intel-cover.png")

W, H = 1600, 900
BG = (10, 10, 10)
ACCENT = (181, 232, 83)
SUBTLE = (138, 138, 138)


def find_mono_font_path() -> str | None:
    for name in ("JetBrains Mono", "DejaVu Sans Mono", "Consolas", "Courier New"):
        try:
            path = font_manager.findfont(name, fallback_to_default=False)
            if path and os.path.exists(path):
                return path
        except Exception:
            continue
    return None


def main() -> None:
    src = Image.open(SRC).convert("RGB")
    sw, sh = src.size
    print(f"Source: {sw}x{sh}")

    crop_right = int(sw * 0.965)
    crop_bottom = int(sh * 0.84)
    cropped = src.crop((0, 0, crop_right, crop_bottom))
    cw, ch = cropped.size
    print(f"Cropped: {cw}x{ch}")

    inner_w = int(W * 0.88)
    inner_h = int(H * 0.74)
    scale = min(inner_w / cw, inner_h / ch)
    new_w = int(cw * scale)
    new_h = int(ch * scale)
    resized = cropped.resize((new_w, new_h), Image.LANCZOS)
    print(f"Resized: {new_w}x{new_h}")

    canvas = Image.new("RGB", (W, H), BG)
    x = (W - new_w) // 2
    y = int(H * 0.13)
    canvas.paste(resized, (x, y))

    draw = ImageDraw.Draw(canvas)
    frame_inset = 4
    draw.rectangle(
        [x - frame_inset, y - frame_inset, x + new_w + frame_inset - 1, y + new_h + frame_inset - 1],
        outline=ACCENT,
        width=2,
    )

    font_path = find_mono_font_path()
    title_size = 30
    caption_size = 16
    if font_path:
        title_font = ImageFont.truetype(font_path, title_size)
        caption_font = ImageFont.truetype(font_path, caption_size)
    else:
        title_font = ImageFont.load_default()
        caption_font = ImageFont.load_default()

    title = "Agentic External Intelligence Platform"
    tw = draw.textlength(title, font=title_font)
    draw.text(((W - tw) / 2, 38), title, fill=(255, 255, 255), font=title_font)

    sub = "Live RAG dashboard  ·  218 sources  ·  tomato-intel-api.onrender.com"
    sw_text = draw.textlength(sub, font=caption_font)
    draw.text(((W - sw_text) / 2, H - 50), sub, fill=ACCENT, font=caption_font)

    canvas.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
