"""
Render 1600x900 cover for the Operations & Production Planning case study.

Four-step flow showing how the planning system works: Inputs -> Engine -> Validate -> Plan.
Dark theme matches the other case-study covers for visual coherence across the portfolio grid.
A planning system with scenario testing, not a statistical forecast.
"""
from __future__ import annotations

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib import font_manager

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(SITE_ROOT, "assets", "images", "projects", "veginova-operations-cover.png")

BG = "#FFFFFF"
CARD = "#0A0A0A"
BORDER = "#0A0A0A"
ACCENT = "#B5E853"
ACCENT_DARK = "#6B9F1F"
TEXT = "#FFFFFF"
ON_BG_DARK = "#0A0A0A"
ON_BG_SUBTLE = "#666666"
DIM = "#B0B0B0"
SUBTLE_NUM = "#8A8A8A"

W, H = 1600, 900


def pick_fonts() -> tuple[str, str]:
    available = {f.name for f in font_manager.fontManager.ttflist}
    title = "Inter" if "Inter" in available else ("DejaVu Sans" if "DejaVu Sans" in available else "sans-serif")
    mono = "JetBrains Mono" if "JetBrains Mono" in available else ("DejaVu Sans Mono" if "DejaVu Sans Mono" in available else "monospace")
    return title, mono


BOXES = [
    {
        "num": "01",
        "title": "Inputs",
        "sub": "Refreshed, not retyped",
        "detail": [
            "Expected sales",
            "Stock on hand",
            "Incoming production",
            "From the warehouse sheet",
        ],
    },
    {
        "num": "02",
        "title": "Engine",
        "sub": "One SQL view, not DAX",
        "detail": [
            "produce-to-safety,",
            "floored at zero",
            "ending = stock + in - sales",
            "red / green per variety",
        ],
    },
    {
        "num": "03",
        "title": "Validate",
        "sub": "Against the planner's sheet",
        "detail": [
            "Reproduces their numbers",
            "0 mismatches",
            "Red can still need 0",
            "(it covers its own sales)",
        ],
    },
    {
        "num": "04",
        "title": "Plan",
        "sub": "Live and forward-looking",
        "detail": [
            "What to produce, when",
            "1-year lead time, seen early",
            "What-if scenarios",
            "Need vs the batch plan",
        ],
    },
]


def main() -> None:
    title_font, mono_font = pick_fonts()
    print(f"Fonts: title={title_font}, mono={mono_font}")

    fig = plt.figure(figsize=(16, 9), facecolor=BG, dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_facecolor(BG)
    ax.axis("off")

    ax.text(60, H - 70, "Operations & Production Planning",
            fontsize=30, color=ON_BG_DARK, fontname=title_font, fontweight="bold")
    ax.text(60, H - 110, "What to produce, how much, and when  ·  validated against the planner's own numbers",
            fontsize=15, color=ON_BG_SUBTLE, fontname=mono_font)

    n = len(BOXES)
    margin = 60
    gap = 28
    total_gap = gap * (n - 1)
    box_w = (W - 2 * margin - total_gap) / n
    box_h = 410
    box_y = (H - box_h) / 2 - 30

    for i, b in enumerate(BOXES):
        x = margin + i * (box_w + gap)
        rect = FancyBboxPatch(
            (x, box_y), box_w, box_h,
            boxstyle="round,pad=0,rounding_size=14",
            linewidth=1.4, edgecolor=BORDER, facecolor=CARD, zorder=2,
        )
        ax.add_patch(rect)

        ax.text(x + 26, box_y + box_h - 50, b["num"],
                fontsize=14, color=SUBTLE_NUM, fontname=mono_font, va="top")
        ax.text(x + 26, box_y + box_h - 88, b["title"],
                fontsize=26, color=TEXT, fontname=title_font, fontweight="bold", va="top")

        ax.plot([x + 26, x + 70], [box_y + box_h - 130, box_y + box_h - 130],
                color=ACCENT, linewidth=2.5, zorder=3, solid_capstyle="round")
        ax.text(x + 26, box_y + box_h - 165, b["sub"],
                fontsize=13, color=ACCENT, fontname=mono_font, va="top")

        for j, line in enumerate(b["detail"]):
            ax.text(x + 26, box_y + box_h - 215 - j * 26, line,
                    fontsize=12, color=DIM, fontname=mono_font, va="top")

        if i < n - 1:
            arrow_x_start = x + box_w + 2
            arrow_x_end = x + box_w + gap - 2
            arrow_y = box_y + box_h / 2
            arr = FancyArrowPatch(
                (arrow_x_start, arrow_y), (arrow_x_end, arrow_y),
                arrowstyle="-|>", mutation_scale=22,
                color=ON_BG_DARK, linewidth=2.6, zorder=3,
            )
            ax.add_patch(arr)

    callout_y = box_y - 70
    ax.plot([60, 90], [callout_y + 8, callout_y + 8], color=ACCENT_DARK, linewidth=3, solid_capstyle="round")
    ax.text(105, callout_y, "Planning system with scenario testing",
            fontsize=14, color=ACCENT_DARK, fontname=mono_font, fontweight="bold", va="center")
    ax.text(105, callout_y - 28,
            "The logic lives in SQL  ·  Power BI renders only  ·  not a statistical forecast",
            fontsize=13, color=ON_BG_SUBTLE, fontname=mono_font, va="center")

    ax.text(W - 60, 40, "SQL  ·  Python  ·  Supabase  ·  Power BI",
            fontsize=12, color=ON_BG_SUBTLE, fontname=mono_font, ha="right", va="center")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=100)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
