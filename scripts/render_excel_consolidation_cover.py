"""
Render a 1600x900 cover for the "From 11 Excel files to one source of truth" case study.

Layout is deliberately different from the finance and operations covers: a column of messy
source files on the left, a funnel arrow through a cleaning step in the middle, and one clean
dashboard panel on the right. It illustrates the method (many files in, one screen out) rather
than mocking a dashboard, because the dashboard for this build does not exist yet.
"""
from __future__ import annotations

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrow
from matplotlib import font_manager

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(SITE_ROOT, "assets", "images", "projects", "excel-to-one-source-cover.png")

BG = "#0B0B0C"
PANEL = "#161618"
PANEL_EDGE = "#2A2A2E"
ACCENT = "#B5E853"
GREEN = "#4ADE80"
RED = "#F26D6D"
TEXT = "#F4F4F5"
DIM = "#9AA3AF"

W, H = 1600, 900


def pick_fonts():
    av = {f.name for f in font_manager.fontManager.ttflist}
    title = "Inter" if "Inter" in av else ("DejaVu Sans" if "DejaVu Sans" in av else "sans-serif")
    mono = "JetBrains Mono" if "JetBrains Mono" in av else ("DejaVu Sans Mono" if "DejaVu Sans Mono" in av else "monospace")
    return title, mono


def panel(ax, x, y, w, h, r=16, edge=PANEL_EDGE, face=PANEL):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                linewidth=1.2, edgecolor=edge, facecolor=face, zorder=2))


def main():
    tf, mf = pick_fonts()
    fig = plt.figure(figsize=(16, 9), facecolor=BG, dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_facecolor(BG)
    ax.axis("off")

    # ── header ──
    ax.text(60, H - 64, "From 11 Excel files to one source of truth", fontsize=30, color=TEXT,
            fontname=tf, fontweight="bold")
    ax.text(60, H - 104, "one folder in  ·  one dashboard out  ·  nobody retypes anything",
            fontsize=14, color=DIM, fontname=mf)
    ax.text(W - 60, H - 64, "Power Query", fontsize=13, color=ACCENT, fontname=mf, ha="right", va="center")

    # ── LEFT: the messy monthly files ──
    fx, fw, fh, fg = 60, 380, 74, 14
    ftop = H - 250
    files = [
        ("2025-01.xlsx", "merged header row", RED),
        ("2025-02.xlsx", "'Cust.' not 'Customer'", RED),
        ("2025-03.xlsx", "Total row inside data", RED),
        ("2025-04.xlsx", "dates stored as text", RED),
        ("2025-05.xlsx", "amounts as text", RED),
        ("...", "7 more months", DIM),
    ]
    for i, (name, issue, col) in enumerate(files):
        y = ftop - i * (fh + fg)
        panel(ax, fx, y, fw, fh)
        ax.text(fx + 24, y + fh - 26, name, fontsize=14, color=TEXT, fontname=mf, va="center")
        ax.text(fx + 24, y + 24, issue, fontsize=11, color=col, fontname=mf, va="center")

    ax.text(fx, ftop + fh + 24, "THE FOLDER", fontsize=12, color=DIM, fontname=mf, va="center")

    # ── MIDDLE: the cleaning step ──
    cx, cy, cw, ch = 520, 285, 290, 300
    panel(ax, cx, cy, cw, ch, edge=ACCENT)
    ax.text(cx + cw / 2, cy + ch - 40, "One set of rules", fontsize=16, color=ACCENT, fontname=tf,
            fontweight="bold", ha="center", va="center")
    steps = [
        "find the real header",
        "rename by lookup",
        "drop total rows",
        "set types explicitly",
        "tag the source file",
    ]
    for i, s in enumerate(steps):
        ax.text(cx + 26, cy + ch - 92 - i * 40, f"{i + 1}.", fontsize=12, color=ACCENT, fontname=mf, va="center")
        ax.text(cx + 58, cy + ch - 92 - i * 40, s, fontsize=12, color=TEXT, fontname=mf, va="center")

    for x0 in (452, 830):
        ax.add_patch(FancyArrow(x0, 435, 56, 0, width=3, head_width=16, head_length=18,
                                length_includes_head=True, color=ACCENT, zorder=4))

    # ── RIGHT: the one clean screen ──
    dx, dy, dw, dh = 906, 130, 634, 594
    panel(ax, dx, dy, dw, dh)
    ax.text(dx + 28, dy + dh - 36, "One dashboard, updates itself", fontsize=16, color=TEXT,
            fontname=tf, fontweight="bold", va="center")
    ax.text(dx + 28, dy + dh - 64, "illustrative", fontsize=11, color=DIM, fontname=mf, va="center")

    # KPI row
    kw, kh = (dw - 56 - 2 * 16) / 3, 96
    kpis = [("REVENUE", "one figure", ACCENT), ("MARGIN", "by product", TEXT), ("VS LAST YEAR", "same month", GREEN)]
    for i, (lab, sub, col) in enumerate(kpis):
        kx = dx + 28 + i * (kw + 16)
        ky = dy + dh - 190
        panel(ax, kx, ky, kw, kh, r=12, face="#1D1D20")
        ax.text(kx + 18, ky + kh - 28, lab, fontsize=10, color=DIM, fontname=mf, va="center")
        ax.text(kx + 18, ky + 34, sub, fontsize=13, color=col, fontname=tf, fontweight="bold", va="center")

    # monthly bars, this year vs last
    bx0, bx1 = dx + 40, dx + dw - 40
    base = dy + 90
    top = dy + dh - 240
    vals = [0.42, 0.50, 0.61, 0.55, 0.68, 0.74, 0.66, 0.79, 0.85, 0.72, 0.90, 0.97]
    prior = [0.35, 0.44, 0.48, 0.52, 0.55, 0.60, 0.62, 0.63, 0.70, 0.66, 0.74, 0.80]
    slot = (bx1 - bx0) / len(vals)
    for i, (v, p) in enumerate(zip(vals, prior)):
        cxx = bx0 + i * slot
        ax.add_patch(plt.Rectangle((cxx + slot * 0.10, base), slot * 0.34, (top - base) * p,
                                   color="#3A3A40", zorder=3))
        ax.add_patch(plt.Rectangle((cxx + slot * 0.50, base), slot * 0.34, (top - base) * v,
                                   color=ACCENT, zorder=3))
    ax.plot([bx0, bx1], [base, base], color=PANEL_EDGE, linewidth=1.2, zorder=3)
    ax.text(dx + 40, dy + 56, "grey = last year   ·   green = this year", fontsize=11, color=DIM,
            fontname=mf, va="center")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=100)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
