"""Render the CV HTML sources to the PDFs the site links.

Usage:  python cv/build_cv_pdf.py          (run from the repo root)

Renders via Python Playwright (Chromium) when installed, otherwise falls back
to headless Microsoft Edge, which ships with Windows. Both are Chromium, so
the @page CSS in the HTML controls size and margins either way.
"""

import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JOBS = [
    (REPO / "cv" / "rasmus-kampmann-cv.html", REPO / "assets" / "files" / "rasmus-kampmann-cv.pdf"),
    (REPO / "cv" / "rasmus-kampmann-cv-da.html", REPO / "assets" / "files" / "rasmus-kampmann-cv-da.pdf"),
]

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def render_playwright() -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            for src, dst in JOBS:
                page.goto(src.as_uri())
                page.pdf(path=str(dst), prefer_css_page_size=True, print_background=True)
                print(f"playwright: {src.name} -> {dst.relative_to(REPO)}")
            browser.close()
        return True
    except Exception as exc:  # missing browser binary etc.
        print(f"playwright failed ({exc}); falling back to Edge", file=sys.stderr)
        return False


def render_edge() -> bool:
    edge = next((p for p in EDGE_PATHS if Path(p).exists()), None) or shutil.which("msedge")
    if not edge:
        return False
    for src, dst in JOBS:
        cmd = [
            edge, "--headless", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={dst}", src.as_uri(),
        ]
        subprocess.run(cmd, check=True, timeout=120)
        for _ in range(50):  # Edge returns before the file is flushed
            if dst.exists() and dst.stat().st_size > 0:
                break
            time.sleep(0.2)
        print(f"edge: {src.name} -> {dst.relative_to(REPO)}")
    return True


if __name__ == "__main__":
    if not (render_playwright() or render_edge()):
        sys.exit("No renderer available: pip install playwright && playwright install chromium, or install Edge.")
