---
layout: project
title: Cold-to-Customer Outbound Pipeline
tagline: "9-stage Node.js pipeline: company registry → LinkedIn scrape → AI personalisation → CRM"
tools: [Node.js, Claude API, Apify, HeyReach, Airtable, Pipedrive]
outcome_headline: "Processes 50 leads per batch with zero manual work"
outcome_detail: "Qualification, personalisation, routing, and CRM sync — fully automated from raw CVR number to sequenced LinkedIn outreach."
order: 1
cover_emoji: "⚙️"
---

## The Problem

The client needed to reach Danish SMBs on LinkedIn at scale — but generic outreach was getting ignored. Manual research per lead took 15–20 minutes. With a target list of thousands of companies, that was never going to work.

The goal: build a pipeline that could qualify, personalise, and push leads into LinkedIn sequences automatically, using the same signals a skilled SDR would look for — just without the SDR.

## Architecture

Nine stages run sequentially. Each phase reads from and writes back to a central Airtable queue, so any stage can be re-run independently without reprocessing the full batch.

<div class="arch-diagram">
P1  CVR Lookup        →  company form, employees, age, industry, VAT frequency
P2  LinkedIn Scrape   →  current role, experience, education, recent posts (Apify)
P3  AI Analysis       →  ICP assessment, persona classification, hook ranking
P4  DM Generation     →  personalised connection request (5 observation types)
P5  Lead Scoring      →  composite 0–135 score + tier A/B/C
P6  HeyReach Push     →  route to solo (≤5 emp) or growing (>5 emp) campaign
P7  Status Sync       →  pull acceptance / reply status back from HeyReach
P8  CRM Deal Sync     →  create Pipedrive deal on warm reply
P9  KPI Snapshot      →  write weekly funnel metrics to reporting table
</div>

## The DM Personalisation Engine

The hardest part was writing connection requests that didn't read like robots wrote them. The solution was a **4-type observation framework** — each type maps to a different psychological trigger:

```javascript
// Sanitised from production pipeline — P4 DM generation
// Each lead's LinkedIn + CVR signals are classified into one observation type

const OBSERVATION_TYPES = {
  TYPE_1: 'Inspiring / impressive — person is doing something noteworthy right now',
  TYPE_2: 'Parallel — person is running two distinct ventures simultaneously',
  TYPE_3: 'Past achievement — verifiable accomplishment, not a current role',
  TYPE_4: 'Transition — person has clearly moved FROM one thing TO another',
};

// Hard guard: every observation must be verifiable from input signals.
// If no specific signal exists → fall back to generic role observation.
// NEVER invent, extrapolate, or assume details not in the data.

async function generateConnectionRequest(lead, signals) {
  const observationType = classifyObservation(signals);

  const systemPrompt = buildSystemPrompt(observationType);
  const userPrompt   = buildUserPrompt(lead, signals);

  // Claude Haiku — fast + cheap for high-volume generation
  const raw = await callClaude(systemPrompt, userPrompt, 350, 3, MODEL_HAIKU);
  const parsed = parseStructuredOutput(raw);

  // Structural validation before writing back to queue
  const isValid = (
    parsed.observation?.length >= 10 &&
    parsed.reaction?.length >= 5 &&
    parsed.full_message?.length >= 80
  );

  return isValid ? parsed : { fallback: true, full_message: buildFallback(lead) };
}
```

The output is validated structurally before writing back — if the AI returns something that fails the checks, a deterministic fallback is used rather than sending a bad message.

## Lead Scoring

Every lead gets a composite score across three dimensions:

| Dimension | Max Points | Signals |
|-----------|-----------|---------|
| ICP Fit | 50 | Company form, employee count, industry, region |
| Intent | 60 | CVR age, job postings, accounting software detected, propensity model score |
| Engagement | 25 | Lookalike to won customers, LinkedIn connection depth |

Leads scoring ≥90 go to campaign A (high-touch); 70–89 to campaign B; below that are queued but deprioritised.

## Customer Exclusion

The pipeline loads a list of 621 current customers (CVR numbers from Pipedrive won deals) on startup. Any match is silently skipped — preventing outbound to existing clients.

```javascript
const CUSTOMER_CVRS = new Set(
  JSON.parse(fs.readFileSync('current_customers.json')).map(c => c.cvr)
);

// In P6 — before any push
if (CUSTOMER_CVRS.has(lead.cvr)) {
  log.info(`[P6] Skipping ${lead.cvr} — existing customer`);
  continue;
}
```

## Results

<div class="result-box">
  <div class="result-label">Outcomes</div>
  <ul>
    <li>Full batch of 50 leads processed in ~12 minutes end-to-end</li>
    <li>Personalised DMs with real LinkedIn signals — not mail-merge templates</li>
    <li>Warm replies automatically routed to Pipedrive as active deals</li>
    <li>Dry-run mode allows safe testing without writing to live systems</li>
  </ul>
</div>

## Key Lessons

**Right-size the AI model.** Haiku is fast and cheap enough to call once per lead at scale; Sonnet is reserved for complex analysis where quality outweighs cost.

**Fail safely.** Every stage that calls an external API has a deterministic fallback. The pipeline continues even if one lead's enrichment fails — it doesn't block the whole batch.

**Observable pipelines save time.** Writing phase-level logs and live funnel counts to Airtable meant debugging a bad batch took minutes, not hours.
