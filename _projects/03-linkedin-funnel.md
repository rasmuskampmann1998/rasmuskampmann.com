---
layout: project
title: LinkedIn Full-Funnel ICP Analytics
tagline: "Connection-to-close funnel analysis across 3,748 LinkedIn contacts"
tools: [Python, pandas, Plotly, Airtable API, Pipedrive API]
outcome_headline: "Identified 538 unmessaged post-engagers + ICP segments with 60.9% win rate"
outcome_detail: "Answered the hardest GTM question: which types of companies actually convert on LinkedIn, and at which stage are we losing them?"
order: 3
cover_emoji: "📊"
---

## The Problem

The client had 3,748 LinkedIn connections built up over years of outreach — but no visibility into which ones had converted, which were in-pipeline, and which were ghosts. Without that data, it was impossible to know:

- Which ICP segments (company size, industry, form) had the highest conversion rates
- Where in the funnel most drop-off was happening
- Which outreach approaches (personal DMs vs. automated sequences) were actually closing deals

The goal was to join LinkedIn contact data, outreach history, and CRM outcomes into a single analytical view.

## Data Architecture

Four datasets are joined on a CVR bridge — company registration number is the shared key across systems:

<div class="arch-diagram">
thread_classification.csv   →  3,748 LinkedIn connections + message history
leads_queue (Airtable)      →  enriched outreach data (CVR, score, pipeline stage)
dim_company (110k rows)     →  firmographic data from company registry
deals (Pipedrive)           →  6,322 deals with source, stage, and won/lost status
</div>

## Thread Classification

Every LinkedIn thread is classified into one of five categories using message content and CRM status:

```python
# Sanitised from customer_journey.py
CLASSES = {
    'KUNDE':  'Confirmed paying customer (matched to Pipedrive won deal)',
    'LEAD':   'Active pipeline — deal open or in conversation',
    'GHOST':  'Connected but never replied to any message',
    'PEER':   'Industry peer / competitor — not a prospect',
    'STOJ':   'Noise — recruiter, irrelevant connection, spam',
}

# Funnel metrics computed per ICP dimension
def funnel_by(df, dim_col):
    """Conversion rates at each stage, grouped by a firmographic dimension."""
    df = df.copy()
    df['has_conversation'] = df['total_msgs'].fillna(0) > 0
    df['has_reply']        = df['inbound'].fillna(0) > 0
    df['has_deal']         = df['cls'].isin(['LEAD', 'KUNDE'])
    df['is_customer']      = df['cls'] == 'KUNDE'

    return df.groupby(dim_col).agg(
        n_connected     = (dim_col, 'count'),
        n_conversation  = ('has_conversation', 'sum'),
        n_replied       = ('has_reply', 'sum'),
        n_deal          = ('has_deal', 'sum'),
        n_customer      = ('is_customer', 'sum'),
    ).assign(
        conv_rate    = lambda x: x.n_conversation / x.n_connected,
        reply_rate   = lambda x: x.n_replied       / x.n_connected,
        deal_rate    = lambda x: x.n_deal           / x.n_connected,
        win_rate     = lambda x: x.n_customer       / x.n_deal.clip(lower=1),
    )
```

## Key Findings

**By company form:** ApS (limited liability) companies had the highest deal rate at 4.2% vs. ENK (sole traders) at 1.1%. Personal outreach to sole traders converts at less than a quarter of the rate — a direct input into ICP scoring weights.

**By employee count:** The 5–19 employee band had a 60.9% win rate once a deal was opened — confirming the "growing SMB" hypothesis. Micro-businesses (0–1 employee) had high connection acceptance but less than 1% deal rate.

**Personal vs. automated:** Morten's personal DMs had a 22% reply rate vs. 8% for HeyReach sequences. But personal messages don't scale — the data was used to identify *which* leads warranted personal outreach (high-score, warm signals) vs. automated sequences.

**Untapped opportunity:** 538 people who had engaged with LinkedIn posts (liked, commented) had never been sent a DM. These were exported as a priority re-engagement list.

## Re-Engagement Scoring

Each connection was scored 0–100 across three dimensions to prioritise outreach:

| Dimension | Max | Signals |
|-----------|-----|---------|
| ICP Fit | 30 | Company form, employee band, industry match |
| Conversation Context | 40 | Reply depth, thread length, last activity recency |
| Content Engagement | 30 | Post likes, comments, engagement recency |

```python
# Score calculation — sanitised
def score_reengagement(row):
    icp_score = (
        ICP_FORM_WEIGHTS.get(row['form_short'], 0) * 0.4 +
        ICP_EMP_WEIGHTS.get(row['emp_band'], 0) * 0.4 +
        ICP_IND_WEIGHTS.get(row['industry_clean'], 0) * 0.2
    ) * 30

    context_score = min(40, (
        (row['inbound'] or 0) * 8 +          # replies received
        min((row['total_msgs'] or 0), 5) * 3 + # conversation depth
        recency_score(row['last_activity'])    # days since last touch
    ))

    engagement_score = min(30, (row['post_engagements'] or 0) * 5)

    return round(icp_score + context_score + engagement_score)
```

## Results

<div class="result-box">
  <div class="result-label">Outcomes</div>
  <ul>
    <li>3,748 connections fully classified and scored</li>
    <li>538 high-intent post-engagers identified as never-messaged</li>
    <li>ICP weights updated based on empirical win rates (not assumptions)</li>
    <li>Top-50 re-engagement list generated with previous DM context included</li>
    <li>Funnel waterfall: connection → DM → reply → deal → won, by 8 dimensions</li>
  </ul>
</div>

## Key Lessons

**A CVR bridge unlocks everything.** LinkedIn connections alone have no firmographic context. Adding company registration numbers as the join key made it possible to cross-reference against 110k companies and CRM data simultaneously.

**Build the waterfall, not just the win rate.** Win rate by segment is misleading without knowing the denominator at each stage. A segment with a 50% win rate but a 0.5% deal rate is still a dead end.

**Post engagers are warm leads.** 538 people had already signalled interest by engaging with content — they just hadn't been contacted. That list had higher reply rates than cold connections.
