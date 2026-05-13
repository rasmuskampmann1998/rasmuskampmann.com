"""
Render 1600x900 cover for the AI Pipeline case study.

The source PNG (ai-pipeline-architecture.png) is 1438x890 with the case study's
dark theme, lime accent, title, and 9-stage architecture already drawn. We pad
it on a 1600x900 #0A0A0A canvas (preserving the source verbatim) so the cover
matches site dimensions without redrawing the diagram.
"""
from __future__ import annotations

import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(SITE_ROOT, "assets", "images", "projects", "ai-pipeline-architecture.png")
OUT = os.path.join(SITE_ROOT, "assets", "images", "projects", "ai-pipeline-cover.png")

BG = (10, 10, 10)
W, H = 1600, 900


def main() -> None:
    src = Image.open(SRC).convert("RGB")
    sw, sh = src.size
    print(f"Source: {sw}x{sh}")

    scale = min(W / sw, H / sh)
    new_w, new_h = int(sw * scale), int(sh * scale)
    resized = src.resize((new_w, new_h), Image.LANCZOS)

    canvas = Image.new("RGB", (W, H), BG)
    x = (W - new_w) // 2
    y = (H - new_h) // 2
    canvas.paste(resized, (x, y))

    canvas.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
