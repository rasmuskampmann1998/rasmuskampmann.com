"""
Render a 1600x900 dashboard-style cover for the Operations & Production Planning case study.

A mock BI dashboard (dark canvas) with a DIFFERENT layout from the finance cover: KPI cards on
the left, a horizontal produce-by-variety bar chart, and a red/green status strip. Illustrative
numbers only. Matches the dark-theme family but is visually distinct from the finance cover.
"""
from __future__ import annotations

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib import font_manager

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(SITE_ROOT, "assets", "images", "projects", "veginova-operations-cover.png")

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


def panel(ax, x, y, w, h, r=16):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                linewidth=1.2, edgecolor=PANEL_EDGE, facecolor=PANEL, zorder=2))


def main():
    tf, mf = pick_fonts()
    fig = plt.figure(figsize=(16, 9), facecolor=BG, dpi=100)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H)
    ax.set_facecolor(BG); ax.axis("off")

    # ── header ──
    ax.text(60, H - 64, "Operations & Production Planning", fontsize=30, color=TEXT,
            fontname=tf, fontweight="bold")
    ax.text(60, H - 104, "What to produce, how much, and when  ·  validated against the planner's own numbers",
            fontsize=14, color=DIM, fontname=mf)
    ax.text(W - 60, H - 64, "Power BI", fontsize=13, color=ACCENT, fontname=mf, ha="right", va="center")

    # ── KPI cards down the LEFT (stacked) ── (different layout from finance's top row)
    kpis = [("To produce", "500", "KS", ACCENT),
            ("Needing production", "9", "varieties", TEXT),
            ("Red / at risk", "13", "below safety line", RED)]
    kx, kw, kh, kg = 60, 440, 168, 18
    ktop = H - 300
    for i, (label, val, sub, col) in enumerate(kpis):
        y = ktop - i * (kh + kg)
        panel(ax, kx, y, kw, kh)
        ax.text(kx + 28, y + kh - 32, label.upper(), fontsize=12, color=DIM, fontname=mf, va="top")
        ax.text(kx + 28, y + kh - 92, val, fontsize=40, color=col, fontname=tf, fontweight="bold", va="center")
        ax.text(kx + 28, y + 26, sub, fontsize=11, color=DIM, fontname=mf, va="center")

    # ── produce-by-variety horizontal bars (RIGHT, big) ──
    bx, by, bw, bh = 540, 120, 1000, 460
    panel(ax, bx, by, bw, bh)
    ax.text(bx + 28, by + bh - 34, "Production needed, by variety", fontsize=15, color=TEXT,
            fontname=tf, fontweight="bold", va="top")
    ax.text(bx + 28, by + bh - 58, "red = below the safety line  ·  illustrative", fontsize=11, color=DIM,
            fontname=mf, va="top")
    rows = [("VAR-F", 204, RED), ("VAR-M", 178, RED), ("VAR-C", 134, RED),
            ("VAR-E", 132, GREEN), ("VAR-J", 86, GREEN), ("VAR-O", 43, GREEN), ("VAR-L", 21, GREEN)]
    p0x = bx + 150
    p1x = bx + bw - 70
    top = by + bh - 100
    rh = (top - (by + 40)) / len(rows)
    mxr = max(r[1] for r in rows)
    for i, (lab, v, col) in enumerate(rows):
        yy = top - (i + 0.5) * rh
        wlen = (v / mxr) * (p1x - p0x)
        ax.add_patch(plt.Rectangle((p0x, yy - rh * 0.3), wlen, rh * 0.6, color=col, zorder=3))
        ax.text(p0x - 16, yy, lab, fontsize=12, color=DIM, fontname=mf, ha="right", va="center")
        ax.text(p0x + wlen + 12, yy, str(v), fontsize=12, color=TEXT, fontname=mf, ha="left", va="center")

    # ── red/green status strip (bottom-left, under the KPIs) ──
    sx, sy, sw, sh = 60, 80, 440, 120
    panel(ax, sx, sy, sw, sh)
    ax.text(sx + 28, sy + sh - 28, "Status by variety", fontsize=13, color=TEXT, fontname=tf,
            fontweight="bold", va="top")
    # a strip of 22 cells, 13 red / 9 green
    statuses = [RED] * 13 + [GREEN] * 9
    cell = (sw - 56) / len(statuses)
    cy = sy + 26
    for i, c in enumerate(statuses):
        ax.add_patch(plt.Rectangle((sx + 28 + i * cell, cy), cell * 0.82, 26, color=c, zorder=3))
    ax.text(sx + 28, sy + 16, "13 red", fontsize=10, color=RED, fontname=mf, va="center")
    ax.text(sx + sw - 28, sy + 16, "9 green", fontsize=10, color=GREEN, fontname=mf, va="center", ha="right")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=100)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
