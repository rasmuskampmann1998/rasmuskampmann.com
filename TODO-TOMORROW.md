# Portfolio — finish tomorrow

**Status as of 2026-06-26 (commit `2c4d3fa`, deployed live, Pages success):**
The site is coherent and the four existing pieces are polished + reordered. The **two Veginova
case studies are drafted and committed but held behind `coming_soon: true`** — they render as
teaser cards only, so the illustrative placeholder numbers are NOT publicly visible yet.
Plan file: `~/.claude/plans/portfolio-completion-plan-lively-cupcake.md`.

**The portfolio is functionally complete the moment the two Veginova pieces flip live.**
After that → START APPLYING. Phases 3–4 are parallel polish, never blockers.

---

## The publish-blockers (only these stop the two Veginova pieces going live)

Files:
- `_projects/04-veginova-invoices.md` (Invoice & Financial Dashboard)
- `_projects/03-veginova-operations.md` (Operations & Production Planning)

### 1. Resolve the placeholder numbers (10 spots total)
Each illustrative number carries an invisible `<!-- PLACEHOLDER: ... -->` comment.
Decide per number: swap in the real figure, OR keep it illustrative permanently.
- Finance piece: 6 placeholders — per-product margin spread, customer concentration, AR total +
  ageing split, time saved, recovered/overdue AR, the recommendation line.
- Operations piece: 4 placeholders — count of at-risk varieties, produce count/quantity, time
  saved, the recommendation line.
- **If keeping them illustrative:** the opening disclaimer already says so (like the Cold-Call
  synthetic note) — just confirm the wording reads right. **Real anchors stay real:**
  2,312,690 DKK / 1.25% reconcile and 22/22 validation are NOT placeholders, leave them.
- Find every spot fast: search both files for `PLACEHOLDER`.

### 2. Confirm/replace the two recommendations
Each piece ends on a recommendation marked with a PLACEHOLDER comment. Make each true to the
real engagement — the specific decision the system enabled. This is the "so what" the rubric
requires; don't ship a generic one.

### 3. Capture the 4 Power BI screenshots (Rasmus, in Desktop)
Each `<!-- SCREENSHOT NEEDED: ... -->` names the exact page to capture. Save into
`assets/images/projects/` with the filename already referenced in the `![...]({{ ... }})` tag.
- Finance: `veginova-finance-overview.png` (Overview/P&L Revenue page),
  `veginova-finance-receivables.png` (Receivables/AR ageing page).
- Operations: `veginova-operations-production.png` (Production red/green page),
  `veginova-operations-need-vs-plan.png` (Need-vs-Plan comparison).
- Also set the card `cover_image` (currently `veginova-invoices.jpg` /
  `veginova-operations.jpg`) — point to a real image or one of the screenshots.

### 4. Flip live + final checks
- Set `coming_soon: true` → `false` in BOTH front matters. (This is what makes the full
  articles render — until then they're cards only.)
- Run both pieces against `Portfolio_Writing_Rubric.md` (the 5 checks) one last time.
- Number-integrity: don't let all-time revenue (7,975,281) be read as the 2024 reconcile target
  (2,312,690); margin shown is **contribution (Dækningsbidrag), ~91.5% on seed sales**, NOT
  profit and NOT the all-revenue 95.5%.
- Commit + push to `main`. Pages auto-deploys (~40s). Verify live with a fetch of
  rasmuskampmann.com: both cards now open to full articles, screenshots render.

---

## After the pieces are live
- **Apply.** The portfolio is done. Phases below happen in parallel, not before.
- Phase 3 (optional, timeboxed ≤1h): colour/theme the screenshots via `Veginova_Green_chrome.json`
  so they look intentional — cosmetic only, do not rebuild reports.
- Phase 4 (ring-fenced, must NOT start before pieces are live): `rasmus-skills` repo file cleanup
  for throughput only — see plan file. If it's happening before the Veginova pieces ship, that's
  the avoidance trap; stop and ship first.

## Housekeeping
- `index.md.bak` is the pre-edit backup of `index.md` (local only, gitignored-by-omission /
  untracked). Delete it once you're happy the site is right.
- No local Ruby/Jekyll toolchain on this machine → no local `jekyll serve`. Verify via the live
  Pages deploy (or install the toolchain if you want a local preview).

## Done 2026-06-26 (don't redo)
Slogan locked 4 places · location Odense · roles analyst-first · outcome numbers surfaced ·
over-claim softened · B2B cut · order fixed (synthetic pieces separated) · Software ML + Tomato
each gained a business recommendation before the retro · both Veginova drafts written, voice-
checked (0 banned terms), committed.
