---
layout: project
title: Market Intelligence Platform
tagline: "Real-time competitive and market intelligence: 812 sources, 495 articles interpreted daily"
tools: [FastAPI, Python, Supabase, Apify, APScheduler, Docker, OpenAI]
outcome_headline: "Monitors crop prices, regulations, and competitor moves across 27 countries — automated"
outcome_detail: "Replaces a daily manual briefing process with a continuously updated intelligence dashboard and weekly PDF report."
order: 6
cover_emoji: "🌍"
---

## The Problem

An agricultural technology client needed continuous visibility across a fragmented intelligence landscape: crop price movements, regulatory changes in 27 countries, competitor product launches, patent filings, and social media signals — simultaneously.

Manual monitoring was a full-time job that still produced incomplete, stale briefings. The goal was to build a platform that collected, processed, and interpreted this information automatically, surfacing only what was relevant.

## Architecture

A FastAPI backend with APScheduler orchestrates scrapers, runs AI interpretation, and stores structured results in Supabase. Everything runs in Docker — portable and infrastructure-agnostic.

<div class="arch-diagram">
Scheduler (APScheduler)
  │
  ├─ Data Collection Layer
  │    ├─ Crop price APIs        →  real-time commodity prices
  │    ├─ Regulatory PDF parser  →  27-country regulatory PDFs → structured text
  │    ├─ Patent database scraper→  agricultural IP filings
  │    ├─ News aggregator        →  RSS + web scrape, 812 sources
  │    └─ Social scrapers        →  LinkedIn, Facebook, Instagram, Twitter, Reddit
  │
  ├─ AI Interpretation Layer (OpenAI)
  │    ├─ Alert classification   →  price spike | disease outbreak | weather event
  │    ├─ Competitor move tagger →  product launch | partnership | market entry
  │    └─ Regulatory delta       →  change summary + compliance impact
  │
  └─ Output Layer
       ├─ Supabase (structured storage)
       ├─ REST API (FastAPI, port 8004)
       ├─ Dashboard (web UI)
       └─ Weekly PDF report (automated)
</div>

## Intelligence Domains

**Alerts** — Crop price spikes, disease outbreaks, and extreme weather events are classified and ranked by business impact. High-severity alerts trigger immediate notifications; others are batched into the daily digest.

**Genetics & Breeding** — Trait databases and breeding trial results from public sources are scraped and tagged by crop type, trait (yield, disease resistance, drought tolerance), and geographic relevance.

**Patents** — New agricultural IP filings are monitored across major patent databases. Competitor patent clusters signal R&D direction before products launch.

**Regulations** — 27-country regulatory landscape tracked via official government sources and EU databases. PDF documents are parsed into structured summaries with change-detection to surface only what's new.

**Competitor Intelligence** — Product announcements, pricing changes, partnership announcements, and hiring patterns (as a proxy for strategic direction) across identified competitors.

## Alert Classification

```python
# Sanitised alert classification — runs on each ingested article

ALERT_SCHEMA = {
    "alert_type": "price_spike|disease|weather|regulatory|competitor",
    "severity": "low|medium|high|critical",
    "crops_affected": ["list of crop names"],
    "regions_affected": ["list of country/region codes"],
    "summary": "One sentence — what happened and why it matters",
    "action_required": "boolean",
    "confidence": 0.0  # 0–1, LLM self-assessed
}

async def classify_alert(article_text: str, source_metadata: dict) -> dict:
    """Classify an ingested article as a business-relevant alert."""
    prompt = f"""
    You are an agricultural intelligence analyst.
    Classify this article and return ONLY valid JSON matching this schema:
    {json.dumps(ALERT_SCHEMA, indent=2)}

    Article: {article_text[:3000]}
    Source: {source_metadata.get('domain')} | {source_metadata.get('region')}
    """
    response = await openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
```

## Data Pipeline

Sources are queried on staggered schedules to balance freshness against API rate limits:

| Source Type | Frequency | Volume |
|-------------|-----------|--------|
| Commodity prices | Every 15 min | 40+ markets |
| News / RSS | Hourly | 812 sources |
| Regulatory PDFs | Daily | 27 countries |
| Social media | 4× daily | 5 platforms |
| Patent databases | Weekly | 3 databases |

Deduplification runs on ingestion — the same story covered by 10 sources is stored once, with source count as a signal for significance.

## Output: Weekly PDF Report

Every Monday, a PDF briefing is generated covering the past 7 days. Structure:

1. Executive summary (3 bullets — highest-impact events)
2. Price movements (charts, % change vs. 4-week average)
3. Regulatory changes (by country, with delta summary)
4. Competitor activity (tagged by company + move type)
5. Research & patent filings (by crop + trait)
6. Social media sentiment (net sentiment by platform + crop)

The PDF is generated programmatically from the Supabase data — no manual assembly.

## Results

<div class="result-box">
  <div class="result-label">Outcomes</div>
  <ul>
    <li>812 sources monitored continuously — vs. 30–40 in the manual process</li>
    <li>495 articles interpreted per day on average</li>
    <li>Alert-to-notification latency: under 90 minutes for critical events</li>
    <li>27-country regulatory coverage — previously manual, now automated</li>
    <li>Weekly PDF report fully automated — zero manual preparation</li>
    <li>Docker deployment: portable, reproducible, runs on any cloud provider</li>
  </ul>
</div>

## Key Lessons

**Structured output is the contract.** Every AI call uses `response_format: json_object` and a named schema. This means the storage layer never needs to parse or interpret — it just validates and writes.

**Coverage breadth beats depth on alert detection.** Monitoring 812 sources at shallow depth catches more actionable signals than deep-reading 50 sources. AI interpretation handles the depth.

**Build the feedback loop early.** Alert quality improved significantly once analysts could mark alerts as relevant/irrelevant — that signal was fed back into classification thresholds within the first two weeks.
