---
layout: project
title: RevOps Data Warehouse
tagline: "Single source of truth: 387k rows from 12 sources → 60+ analysis outputs in one pull"
tools: [Python, Node.js, Airtable, Pipedrive, pandas, Plotly]
outcome_headline: "Replaced 10h/week of manual reporting — full GTM visibility in 27 seconds"
outcome_detail: "One command pulls all data, runs all analyses, and writes 60+ CSV outputs. No spreadsheets, no copy-paste, no stale numbers."
order: 4
cover_emoji: "🗄️"
---

## The Problem

The GTM team's data was scattered: leads in Airtable, deals in Pipedrive, call history in a separate CRM, ML outputs in local CSVs, and KPIs in a spreadsheet that someone updated manually each Monday. Getting a coherent view of pipeline health took half a morning.

The goal was a single-command data pull that joined all sources, ran the full suite of analyses, and produced clean outputs — without touching a spreadsheet.

## Data Architecture

All 12 sources are catalogued in a `manifest.json` that records file paths, primary keys, expected row counts, and staleness thresholds:

```json
{
  "sources": {
    "dim_company": {
      "path": "cold_calling/dim_company.csv",
      "pk": "CVR",
      "rows_expected": 110164,
      "stale_after_days": 7,
      "description": "Full company registry — 110k Danish SMBs with firmographics"
    },
    "fact_deals": {
      "path": "crm/deals.csv",
      "pk": "Deal ID",
      "rows_expected": 6322,
      "stale_after_days": 1,
      "description": "Pipedrive deals — source, stage, value, won/lost"
    },
    "leads_queue": {
      "path": "operations/leads_queue.csv",
      "pk": "record_id",
      "rows_expected": 1072,
      "stale_after_days": 1,
      "description": "Active outbound queue — scored, tiered, pipeline stage"
    }
  }
}
```

The manifest serves as both documentation and a data quality gate — the pull script warns on stale files before running analyses.

## Data Pull

Two modes depending on what's needed:

```python
# pull_data.py — sanitised
# --local : read from disk only (27s)
# --full  : re-fetch from all APIs before reading (90s)

def pull_all(mode='local'):
    manifest = load_manifest()
    results  = {}

    for source_name, meta in manifest['sources'].items():
        path = DATA_DIR / meta['path']

        if mode == 'full' and meta.get('api_source'):
            # Fetch fresh from Airtable / Pipedrive API
            fetch_from_api(source_name, meta, path)

        if not path.exists():
            warn(f"Missing: {source_name} — skipping downstream analyses")
            continue

        age_days = (datetime.now() - datetime.fromtimestamp(path.stat().st_mtime)).days
        if age_days > meta['stale_after_days']:
            warn(f"Stale ({age_days}d): {source_name}")

        results[source_name] = pd.read_csv(path, low_memory=False)
        print(f"  ✓ {source_name}: {len(results[source_name]):,} rows")

    return results
```

## Analysis Suite (60+ Outputs)

Every analysis is a standalone script that reads from the pulled data and writes a CSV. Running them all takes under 30 seconds on a local machine.

| Category | Outputs |
|----------|---------|
| Meeting funnel | Conversion by software, company form, employees, industry, region, revenue, source, closer |
| Cold call | Outcomes by status, win rate by form/industry/region/rep, intensity heatmap |
| LinkedIn ICP | Funnel waterfall, personal vs. auto comparison, deal velocity, re-engagement scores |
| Churn timeseries | Churn by software, form, industry, source; monthly + YoY trends; cohort retention matrix |
| Lead scoring | Tier distribution, score percentiles, propensity model performance |
| MRR | By customer segment, software, industry, employee band |

## Dashboards

Three interactive HTML dashboards are generated from the analysis outputs:

**Meeting Funnel Dashboard** — Plotly charts for each conversion dimension. Filter by date range, source, or closer. Key metric: close rate by accounting software in use before switching.

**Cold Call Analysis Dashboard** — Call outcomes vs. expected outcomes by segment. Identifies where conversion is above/below baseline.

**Unified ICP Dashboard** — Combines LinkedIn funnel + meeting funnel + cold call overlay. Single view of which company profiles convert best across all channels.

```python
# Dashboard generation — sanitised
def build_meeting_funnel_dashboard(df_meetings, df_deals):
    """Generate interactive HTML dashboard from analysis CSVs."""
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=[
            'Close Rate by Accounting Software',
            'Win Rate by Employee Band',
            'Conversion by Company Form',
            'Monthly Wins Trend',
            'Lost Deal Reasons',
            'Time to Close by Source',
        ]
    )
    # Each subplot pulls from a pre-computed analysis CSV
    add_software_chart(fig, df_meetings, row=1, col=1)
    add_emp_chart(fig, df_meetings, row=1, col=2)
    # ... etc.

    fig.write_html(OUTPUT_DIR / 'meeting_dashboard.html')
```

## Results

<div class="result-box">
  <div class="result-label">Outcomes</div>
  <ul>
    <li>387,902 rows across 12 sources joined in a single pull</li>
    <li>Local mode: full data refresh in 27 seconds</li>
    <li>60+ analysis CSVs covering every GTM dimension</li>
    <li>3 interactive HTML dashboards — no BI tool license required</li>
    <li>Weekly KPI snapshot automated via GitHub Actions (Monday 08:00 CET)</li>
  </ul>
</div>

## Key Lessons

**A manifest beats a README.** Documenting data sources in a machine-readable format means the pull script can self-validate — no more "is this file current?" questions.

**Separate the pull from the analysis.** Fetching data and running analyses are different concerns. Local-mode lets you iterate on analytics without waiting for API calls.

**Ship dashboards as HTML files.** No server, no BI tool subscription, no login. An HTML file in a shared folder is the fastest path from analysis to stakeholder.
