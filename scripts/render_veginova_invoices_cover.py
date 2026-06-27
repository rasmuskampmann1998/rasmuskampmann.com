"""
Render a 1600x900 dashboard-style cover for the Invoice & Financial Dashboard case study.

A mock BI dashboard (dark canvas): KPI cards + revenue-by-month bars + an AR-ageing panel.
Illustrative numbers only (no real client figures). Matches the portfolio's dark-theme family
but reads as a dashboard, not an abstract flow diagram. Visually distinct from the operations cover.
"""
from __future__ import annotations

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib import font_manager

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(SITE_ROOT, "assets", "images", "projects", "veginova-invoices-cover.png")

BG = "#0B0B0C"          # dark dashboard canvas
PANEL = "#161618"        # card panels
PANEL_EDGE = "#2A2A2E"
ACCENT = "#B5E853"       # lime
GREEN = "#4ADE80"
AMBER = "#F5B14C"
RED = "#F26D6D"
TEXT = "#F4F4F5"
DIM = "#9AA3AF"
GRID = "#26262B"

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
    ax.text(60, H - 64, "Invoice & Financial Dashboard", fontsize=30, color=TEXT,
            fontname=tf, fontweight="bold")
    ax.text(60, H - 104, "Profit per product, profit per customer, and the cash owed  ·  reconciled within 1.25%",
            fontsize=14, color=DIM, fontname=mf)
    ax.text(W - 60, H - 64, "Power BI", fontsize=13, color=ACCENT, fontname=mf, ha="right", va="center")

    # ── KPI cards row ──
    kpis = [("Revenue", "5.90M", "DKK", ACCENT),
            ("Contribution", "5.10M", "Dækningsbidrag", GREEN),
            ("Outstanding", "0.89M", "Receivables", AMBER),
            ("Margin", "86%", "Contribution %", TEXT)]
    kx, ky, kw, kh, kg = 60, H - 300, 352, 150, 13
    for i, (label, val, sub, col) in enumerate(kpis):
        x = kx + i * (kw + kg)
        panel(ax, x, ky, kw, kh)
        ax.text(x + 26, ky + kh - 34, label.upper(), fontsize=12, color=DIM, fontname=mf, va="top")
        ax.text(x + 26, ky + kh - 96, val, fontsize=34, color=col, fontname=tf, fontweight="bold", va="center")
        ax.text(x + 26, ky + 24, sub, fontsize=11, color=DIM, fontname=mf, va="center")

    # ── revenue by month (bars) ──
    bx, by, bw, bh = 60, 80, 920, 320
    panel(ax, bx, by, bw, bh)
    ax.text(bx + 26, by + bh - 30, "Revenue by month", fontsize=15, color=TEXT, fontname=tf, fontweight="bold", va="top")
    ax.text(bx + 26, by + bh - 54, "illustrative", fontsize=11, color=DIM, fontname=mf, va="top")
    vals = [235, 322, 318, 262, 332, 484, 278, 285, 265, 452, 358, 190,
            205, 145, 193, 230, 106, 79, 68, 296, 207, 294, 84, 240]
    n = len(vals); plot_x0, plot_x1 = bx + 36, bx + bw - 30
    plot_y0, plot_y1 = by + 36, by + bh - 90
    bar_w = (plot_x1 - plot_x0) / n * 0.66
    mx = max(vals)
    for i, v in enumerate(vals):
        cx = plot_x0 + (i + 0.5) * (plot_x1 - plot_x0) / n
        bhgt = (v / mx) * (plot_y1 - plot_y0)
        ax.add_patch(plt.Rectangle((cx - bar_w / 2, plot_y0), bar_w, bhgt, color=ACCENT, zorder=3))
    ax.text(bx + 26, plot_y0 - 6, "Jan 2024", fontsize=10, color=DIM, fontname=mf, va="top")
    ax.text(bx + bw - 30, plot_y0 - 6, "Dec 2025", fontsize=10, color=DIM, fontname=mf, va="top", ha="right")

    # ── AR ageing panel ──
    ax2x, ax2y, ax2w, ax2h = 1000, 80, 540, 320
    panel(ax, ax2x, ax2y, ax2w, ax2h)
    ax.text(ax2x + 26, ax2y + ax2h - 30, "Accounts receivable by age", fontsize=15, color=TEXT,
            fontname=tf, fontweight="bold", va="top")
    buckets = [("0-30", 35, GREEN), ("31-60", 127, GREEN), ("61-90", 39, AMBER), ("90+", 94, RED)]
    p0x, p1x = ax2x + 40, ax2x + ax2w - 40
    p0y, p1y = ax2y + 48, ax2y + ax2h - 90
    mxb = max(b[1] for b in buckets)
    slot = (p1x - p0x) / len(buckets)
    for i, (lab, v, col) in enumerate(buckets):
        cx = p0x + (i + 0.5) * slot
        bhgt = (v / mxb) * (p1y - p0y)
        bw2 = slot * 0.5
        ax.add_patch(plt.Rectangle((cx - bw2 / 2, p0y), bw2, bhgt, color=col, zorder=3))
        ax.text(cx, p0y + bhgt + 10, f"{v}k", fontsize=11, color=TEXT, fontname=mf, ha="center", va="bottom")
        ax.text(cx, p0y - 8, lab, fontsize=11, color=DIM, fontname=mf, ha="center", va="top")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=100)
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
