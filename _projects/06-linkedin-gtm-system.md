---
layout: project
title: End-to-End B2B GTM System
tagline: "Nine-stage LinkedIn outbound pipeline. Scraping, scoring, AI personalisation, CRM sync, real-time stakeholder reporting. Built for a small team."
tools: [Node.js, Python, Claude API, Apify, HeyReach, Airtable, Pipedrive, PostgreSQL, GitHub Actions]
outcome_headline: "Replaced manual SDR research with an automated pipeline that qualifies, scores, personalises, and routes thousands of leads"
outcome_detail: "Outbound capacity of a three-person SDR team, consistent quality, full CRM observability, weekly stakeholder reporting."
order: 6
cover_image: /assets/images/projects/linkedin-gtm.jpg
---

## The problem

The client wanted to scale LinkedIn outbound, but every lead needed real personalisation to get a reply. Manual SDR research, message drafting, and CRM logging ran around 15 to 20 minutes per lead. The maths doesn't work past the first few hundred contacts.

The brief: a system that does the research, writes the message, sends it on the right cadence, routes warm replies into the CRM as deals, and gives leadership a live view of what's working. Without it sounding like a bot, and without an SDR team to run it.

## What the system does end to end

Nine stages, run as a single Node.js process orchestrated by a small Python control layer. Each stage reads from and writes back to a central queue, so any stage can be rerun independently without reprocessing the full batch.

1. **Data collection.** Pull the latest cohort of target companies from the public Danish company registry. Filter to ICP-fit candidates on a first pass.
2. **Scraping.** Hit LinkedIn through Apify to get current role, experience, recent posts, education. Hit other public sources for jobs, social, news, reviews.
3. **AI analysis.** Claude reads the scraped data through a structured tool-use call. It returns ICP-fit assessment, a persona classification, and a ranked list of possible hooks per person.
4. **Message generation.** A second Claude call drafts the outbound message in the prospect's language, anchored on a verifiable observation about that specific person. No generic compliments. No vendor talk.
5. **Quality validation.** A third Claude call double-checks tone, length, factual accuracy against the source data, em-dash overuse, and AI-pattern tells. If the validation score is below threshold, the message falls back to a deterministic template. Never to a raw AI miss.
6. **Lead scoring.** A composite score across ICP fit (public registry features), intent (job postings, social signals, news), and engagement (existing connection depth). The ML software-detection model from the [previous case study]({{ '/projects/05-software-detection-ml' | relative_url }}) plugs in here.
7. **Customer-exclusion check.** A guardrail that hard-stops outbound to anyone already on the customer list.
8. **Sequence push.** Routed to the right HeyReach campaign based on segment.
9. **CRM sync.** Positive replies land in Pipedrive as deals, negative replies get auto-classified, ambiguous ones get flagged for human review.

## ICP definition

Before any of this runs, the ICP has to be defined sharply. I spent the first phase of the engagement working with the founder to turn "small Danish B2B service businesses" into something the pipeline can act on:

- Hard filters: company form, employee range, founding window, geographic region
- Soft signals: VAT cadence, industry NACE code, technology stack indicators
- Exclusion signals: existing customers, competitor employees, currently in an active conversation

The ICP lives in a versioned config file, not buried in code. When the founder wants to test a new segment, the config gets a new entry and the pipeline picks it up on the next run.

## The personalisation layer

Every message starts from a real, verifiable observation about that specific person. A post they wrote, a hire they made, a tool they use, a milestone they hit. The AI doesn't invent context. It picks one observation, frames it in the prospect's voice, and asks one direct question.

The whole layer runs through a humaniser that strips the patterns I see most often in AI-generated outbound. Em-dash overuse, hollow superlatives, "I hope this finds you well", "not just X but Y" constructions, three-item lists. The output is short, specific, and reads like the founder wrote it himself.

This is where prompt engineering carries the engagement. Five prompts in production, each tuned for a different stage of the pipeline. Each one constrained by structured-output schemas so downstream code can rely on the shape of the JSON. Each one tested against a held-out set of real-world examples before any change is merged.

## How AI gets used

Claude does three jobs in the pipeline:

- **Read the data.** The ICP-fit assessment is a tool-use call that returns structured JSON with reasoning. Downstream code reads the JSON, not the natural-language output.
- **Write the message.** A Haiku-tier model writes the first draft. A second pass against the humaniser brings it into the founder's voice.
- **Validate.** A Sonnet-tier call double-checks tone, length, factual accuracy. Failed messages fall back to a deterministic template.

Every Claude call is right-sized. Haiku for high-volume, low-stakes generation. Sonnet for the harder reasoning steps. Costs stay predictable per lead. Failures fall back to safe defaults rather than crashing the batch.

A lot of the iteration on this system used vibe coding. The model takes a high-level instruction ("rewrite this stage so each phase logs to Airtable with phase-name + run-id"), produces a draft, and I review and merge. The combination of vibe-coded scaffolding plus careful prompt engineering on the user-facing AI calls is what made the build feasible in the time budget.

## Real-time action on data

The pipeline isn't just batch. As replies come in, the system reacts:

- A positive reply triggers an immediate Pipedrive deal creation with the right stage.
- A "send me more info" reply triggers a follow-up sequence in HeyReach.
- An out-of-office gets parsed, the prospect gets snoozed until the return date.
- A clear "not interested" gets logged, the prospect gets added to the suppression list.

Stage transitions happen within minutes of the reply landing. The founder doesn't have to triage manually.

## Stakeholder management and reporting

The founder isn't technical. The pipeline has to be observable without him reading code or SQL.

- A weekly KPI dashboard refreshes every Monday morning. Connections sent, accepted, replied, meetings booked, deals created, won.
- A Scrape Status panel shows source health. If LinkedIn rate-limits a scraper, the panel shows a yellow flag before any leads go missing.
- A weekly auto-generated summary email lands in the founder's inbox on Monday at 09:00. Three paragraphs. Numbers vs. last week. What broke, what to look at.

When something breaks, I get an alert before he does, and the fix-cycle is short. That trust loop is half the engagement.

## What the system runs on

- **Orchestration.** Node.js for the main pipeline, Python for analytics and a small control layer.
- **Scraping.** Apify actors for LinkedIn and Meta. Custom Python for niche sources.
- **AI.** Claude API (Haiku + Sonnet routed by task). Tool-use for structured outputs.
- **Data layer.** Airtable as the operational queue, PostgreSQL for the analytics warehouse, Pipedrive as the CRM destination.
- **Sequencing.** HeyReach for the LinkedIn cadence.
- **Automation.** GitHub Actions for scheduled runs and monthly retraining of the lead-scoring model.

## Business outcome

The outcome was a small team operating with the outbound capacity of three SDRs, at consistent message quality, with a founder who could see exactly what was happening week to week. That's the real product. The technical surface area underneath is just what it took to get there.
