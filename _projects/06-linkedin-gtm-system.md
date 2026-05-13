---
layout: project
title: End-to-End B2B GTM System
tagline: "AI-driven LinkedIn outbound for a small B2B team. Scraping, scoring, personalisation, CRM sync, real-time reply handling, weekly founder reporting. Around 50% cold connection acceptance."
tools: [Node.js, Python, Claude API, Apify, HeyReach, Airtable, Pipedrive, PostgreSQL, GitHub Actions]
outcome_headline: "Replaced an SDR team with a 9-stage pipeline that researches, writes, sends, and routes thousands of leads with a founder in the loop"
outcome_detail: "AI wired into every stage of the funnel. Real-time CRM sync. Weekly auto-generated stakeholder reporting. ~50% acceptance rate on cold connections."
order: 6
cover_image: /assets/images/projects/linkedin-gtm.jpg
github_url: https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies
---

## Outcome first

I built a 9-stage outbound pipeline that gives a single founder the cold-outreach capacity of a small SDR team. AI does the research, drafts the message, validates the tone, and routes warm replies into the CRM as deals. The founder reviews the weekly report on Monday morning.

The headline number: around 50% acceptance rate on cold LinkedIn connections. That's the metric that compounds. Below 30%, the team is just burning sender reputation. Above 45%, conversations actually start.

Every message starts from a verifiable observation about the specific person it's going to, written in the language they post in. No copy-paste templates. The system runs on autopilot. The founder runs the business.

Want the technical deep-dive: pipeline architecture, prompt design, validator logic, deployment? See the [GitHub case study](https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies).

## Context

A Danish SMB accounting firm wanted to scale LinkedIn outbound without hiring SDRs. The founder had been running outbound manually. Acceptance rates were good when he wrote the messages himself, but it was eating 15 to 20 minutes per lead between research, drafting, sending, and CRM logging. The maths doesn't work past the first few hundred contacts.

The brief: a system that does the research, writes the message in the founder's voice, sends it on the right cadence, routes warm replies into the CRM as deals, and gives the founder a live view of what's working. Without sounding like a bot. Without an SDR team to run it.

The constraint that shaped the whole build: every message had to be defensible. If the founder reviewed any single outbound, the personalisation, the tone, and the ask all had to be something he'd actually say.

## The problem

Cold outbound at scale fails for two structural reasons. Manual personalisation doesn't scale past a few hundred contacts. Generic AI outbound gets ignored and gets the sender flagged. Most "AI outbound" tools solve the wrong half: they generate volume, not signal. The output reads like AI because it is AI, and acceptance rates collapse.

For this client specifically:

- The founder was the brand. Anything that sounded off-voice would damage trust faster than no outreach at all.
- The ICP existed in his head but not on paper. Hard filters mixed with soft signals mixed with exclusion lists.
- Manual review of every outbound was non-negotiable in v1. The system had to produce messages the founder would actually approve.

## The approach

I framed the build around four jobs the system had to do. AI gets used where it earns its place. Deterministic logic does the rest.

**Define the ICP as data, not vibes.** The founder's gut sense of "small Danish B2B service businesses" had to become hard filters (company form, employee range, founding window, region), soft signals (VAT cadence, industry codes, tech-stack indicators), and exclusion signals (existing customers, competitors, active conversations). The ICP lives in a versioned config file. When the founder wants to test a new segment, the config gets a new entry. The pipeline picks it up on the next run.

**Score every lead before reaching out.** A composite score across ICP fit (registry features), intent (job postings, social signals, news), and engagement (existing connection depth). The [software-detection ML model]({{ '/projects/05-software-detection-ml' | relative_url }}) plugs in here as a score boost. Reaching out to everyone is cheap. Reaching out to the wrong people is expensive. The score decides the order, and the order matters when the founder has limited weekly capacity.

**Write outreach that survives manual review.** Three Claude calls per lead, each with a different job. Read the data, draft the message, validate the output. The drafts get a humaniser pass that strips AI-pattern tells (em-dash overuse, "I hope this finds you well," three-item lists, "not just X but Y" constructions). If the validator score is below threshold, the message falls back to a deterministic template. Never to a raw AI miss.

**Act on data in real time, not in batch.** A positive reply triggers a Pipedrive deal within minutes. An out-of-office gets parsed and snoozes the prospect until the return date. A "not interested" reply gets logged and added to the suppression list. The founder doesn't triage manually. The system already did.

## The build

```
Public registry → ICP filter → LinkedIn + multi-source scrape
       │
       ▼
   Lead scoring (ICP + intent + engagement + ML boost)
       │
       ▼
   AI personalisation (3 Claude calls per lead)
       │   1. Read the data (tool-use, structured JSON)
       │   2. Draft the message (Haiku, founder voice)
       │   3. Validate the output (Sonnet, schema-checked)
       ▼
   Customer-exclusion guardrail
       │
       ▼
   HeyReach campaign (segment-routed cadence)
       │
       ▼
   Real-time reply handler → Pipedrive (deals + classification)
       │
       ▼
   Weekly KPI dashboard + auto-generated founder email
```

*The 9-stage pipeline. Each stage reads from and writes back to a central queue, so any stage can be rerun independently without reprocessing the full batch.*

Two things matter most in the build.

**The AI layer is three Claude calls, not one.** Cheap models for high-volume drafting, expensive models for harder reasoning. Haiku writes the first draft of every message. Sonnet does the ICP-fit assessment (the call where reasoning matters most) and the validation pass (where catching a bad message matters more than saving a token). The cost stays predictable per lead. Failures fall back to deterministic templates rather than crashing the batch.

The validator is the part most outbound tools skip. It checks tone, length, factual accuracy against the source data, and AI-pattern tells. If a message claims the prospect "recently posted about X" but the scrape didn't actually find that post, the validator catches it. If the message uses three em-dashes in five sentences, the validator catches it. Production prompts are version-controlled and tested against a held-out set of real-world examples before any change merges.

**Every stage is independently rerunnable.** Each writes to a central queue keyed on the lead ID. If the LinkedIn scrape fails for a batch, I rerun stage 2 without touching stages 1, 3, or 4. If a prompt update changes downstream message quality, I rerun stages 4-5 on the existing scrape data. This is the difference between a fragile demo and a system that ships.

![Weekly KPI dashboard the founder reviews every Monday]({{ '/assets/images/projects/linkedin-gtm-dashboard.png' | relative_url }})
*Weekly KPI dashboard. Connections sent, accepted, replied, meetings booked, deals created, won. The founder opens this Monday morning. Numbers anonymised for the public version.*

## The outcome

What changed for the founder:

- He stopped writing outbound. He still reviews it. He doesn't draft it.
- Replies surface in the CRM as deals automatically. No manual logging.
- The Monday morning report tells him what worked last week, what broke, and what to look at. Three paragraphs. Numbers vs. last week.
- When a scraper rate-limits or a stage breaks, the alert reaches me before it reaches him. The trust loop is half the engagement.

The system has the cold-outbound capacity of a small SDR team at consistent message quality. The product is the founder spending his week on conversations that converted, not on the work that gets you to those conversations.

## What I'd do differently

The first version of the validator was too aggressive. It triggered fallbacks to a generic template whenever the AI quality score dipped, even when the underlying message was structurally fine. A meaningful slice of leads were getting the generic version when they should have been getting the personalised one. I caught it in the weekly review and tightened the trigger logic so only hard structural failures fall back to template. The fix taught me a rule I should have built in from day one: every fallback decision needs to be logged with the reason. Observability beats post-hoc debugging every time.

## Tools

Node.js for the main pipeline orchestration. Python for analytics, the ML scoring model, and a small control layer. Claude API (Haiku + Sonnet, routed by task) for the AI layer, with tool-use for structured outputs. Apify for LinkedIn and Meta scraping. Custom Python scrapers for niche sources. Airtable as the operational queue. PostgreSQL for the analytics warehouse. Pipedrive as the CRM destination. HeyReach for the LinkedIn cadence. GitHub Actions for scheduled runs and monthly retraining of the lead-scoring model.
