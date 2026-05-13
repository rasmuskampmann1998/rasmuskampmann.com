---
layout: project
title: End-to-End AI-Driven Data Pipeline
tagline: "Multi-stage system orchestrating scraping, scoring, AI-driven content generation, and real-time data routing. Built around methodology, not metrics. Around 50% cold connection acceptance rate."
tools: [Node.js, Python, Claude API, Apify, Clay, Airtable, PostgreSQL, Pipedrive, HeyReach, GitHub Actions]
outcome_headline: "Nine-stage pipeline combining public data extraction, ML scoring, multi-model AI orchestration, and real-time routing into operational systems"
outcome_detail: "Built around methodology, not metrics. Validator logic, deterministic fallbacks, queue-based stage isolation, multi-model routing. Around 50% cold connection acceptance rate."
order: 6
cover_image: /assets/images/projects/linkedin-gtm.jpg
github_url: https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies
---

## What this case study demonstrates

A nine-stage pipeline that combines public data extraction, ML-based scoring, multi-model AI orchestration with validator logic, and real-time data routing into operational systems. Built for a Danish SMB client. The architecture is the point. The use case is the proof.

Every stage reads from and writes back to a central queue, keyed on the entity ID. Any stage can be rerun independently. Failures degrade gracefully to deterministic fallbacks rather than crashing the batch. AI is used where it earns its place. Deterministic logic does the rest.

Want the technical deep-dive: pipeline architecture, prompt design, validator logic, deployment? See the [GitHub case study](https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies).

## Outcome first

The system runs end-to-end on autopilot. The only human-in-the-loop step is a weekly review of outputs and a Monday-morning summary the system generates automatically.

The one metric that compounds: around 50% acceptance rate on cold LinkedIn connections. Below 30%, the system is burning sender reputation. Above 45%, conversations actually start. The 50% number is what tells me the validator logic and the personalisation layer are working as designed.

Everything else this case study covers is methodology. How the system is structured. Why each component exists. What each AI call is doing. How the validator catches AI-pattern outputs before they ship.

## Context

A Danish SMB needed a data system that could research entities, generate personalised content at scale, route signals into operational tools, and produce weekly performance reporting. The work was being done manually. The structural limit: manual personalisation at scale is impossible. Generic AI output collapses acceptance rates and damages downstream trust.

The brief: a system that does the research, generates personalised content in a defined voice, routes outputs through validation, syncs results into operational systems, and produces a live performance view. Without sounding like a bot. Without an operations team to run it.

The constraint that shaped the build: every output had to be defensible. If reviewed manually, the data, the personalisation, and the structure all had to be something a domain expert would actually approve.

## The problem

Two structural failure modes for systems like this:

- **Manual personalisation doesn't scale.** Past a few hundred entities, the per-record time cost destroys the unit economics.
- **Generic AI output gets ignored.** The output reads like AI because it is AI. Acceptance collapses, trust collapses.

Most "AI-driven" pipelines solve the wrong half. They generate volume, not signal. They optimise for throughput rather than per-record quality. The interesting engineering problem is producing AI output that survives manual review at scale.

## The approach

Four jobs the system has to do. AI gets used where it earns its place. Deterministic logic does the rest.

**Define the target as data, not vibes.** The domain expert's gut sense of "the right entity" had to become hard filters (entity attributes from public registry data), soft signals (behavioural patterns, observable signals), and exclusion signals (existing relationships, suppression lists). The configuration lives in a versioned file. New segments are new entries. The pipeline picks them up on the next run.

**Score every entity before acting.** A composite score across fit (registry features), intent signals (observable activity), and engagement (existing context). The [ML detection model]({{ '/projects/05-software-detection-ml' | relative_url }}) plugs in here as a score boost. Acting on every entity is cheap. Acting on the wrong entities is expensive. The score decides the order.

**Generate output that survives manual review.** Three Claude calls per record, each with a different job. Read the data, draft the output, validate the output. The validator strips AI-pattern tells (em-dash overuse, three-item lists, "not just X but Y" constructions, factual claims not present in source data). If the validator score is below threshold, the output falls back to a deterministic template. Never to a raw AI miss.

**Act on data in real time, not in batch.** Positive signals trigger downstream records in operational systems within minutes. Auto-responses get parsed and snoozed until the return date. Negative signals get logged and added to suppression lists. No manual triage.

## The build

![Nine-stage pipeline architecture]({{ '/assets/images/projects/ai-pipeline-architecture.png' | relative_url }})
*Nine-stage pipeline. Each stage reads from and writes to the central queue. Any stage can be rerun independently.*

Each stage reads from and writes back to a central queue. Any stage can be rerun independently. This is the difference between a fragile demo and a system that ships.

Two things matter most in the build.

**The AI layer is three Claude calls, not one.** Cheap models for high-volume generation, expensive models for harder reasoning. Haiku writes the first draft. Sonnet does the fit assessment (the call where reasoning matters most) and the validation pass (where catching a bad output matters more than saving tokens). Cost stays predictable per record. Failures fall back to deterministic templates rather than crashing the batch.

| Call | Model | Job | Why this model |
|------|-------|-----|----------------|
| 1 | Sonnet | Read and assess fit | Reasoning matters most here |
| 2 | Haiku | Draft output | Cheap, high-volume, fast |
| 3 | Sonnet | Validate and catch failures | Catching bad output is worth the token cost |

**The validator is the part most pipelines skip.** It checks tone, length, factual accuracy against source data, and AI-pattern tells. If an output claims the entity "recently did X" but the scrape didn't actually find that signal, the validator catches it. If the output uses three em-dashes in five sentences, the validator catches it. Production prompts are version-controlled and tested against a held-out set of real-world examples before any change merges.

![Validator decision tree]({{ '/assets/images/projects/ai-pipeline-validator.png' | relative_url }})
*The validator runs four checks before any output ships. Hard structural failures fall back to deterministic templates.*

**Every stage is independently rerunnable.** If the scrape fails for a batch, stage 2 reruns without touching stages 1, 3, or 4. If a prompt update changes downstream output quality, stages 4-5 rerun on the existing scrape data. The system is observable from end to end.

![Queue-based stage isolation]({{ '/assets/images/projects/ai-pipeline-queue.png' | relative_url }})
*Independent rerunnability. A failed stage reruns without reprocessing upstream stages.*

## The outcome

The system runs on autopilot. Manual work shifted from drafting and routing to reviewing and exception-handling. The Monday morning summary tells the domain expert what worked last week, what broke, and what to look at. Three paragraphs. Numbers vs. last week.

![Monday morning summary]({{ '/assets/images/projects/ai-pipeline-summary.png' | relative_url }})
*Auto-generated Monday summary. System metadata: stages run, fallback rate, validator pass rate, queue health. Client-identifying numbers anonymised.*

When a stage breaks, the alert reaches me before it reaches the user. Observability is half the engagement. The other half is the AI orchestration layer. The validator is what makes the AI output trustworthy at volume.

The one number that matters: around 50% acceptance rate on cold outputs. That's the signal that tells me the validator and personalisation layers are working as designed. Everything else this case study describes is the methodology that produces that number.

## What I'd do differently

The first version of the validator was too aggressive. It triggered fallbacks to a generic template whenever the AI quality score dipped, even when the underlying output was structurally fine. A meaningful slice of records were getting the generic version when they should have been getting the personalised one. I caught it in the weekly review and tightened the trigger logic so only hard structural failures fall back to template.

The fix taught me a rule I should have built in from day one: every fallback decision needs to be logged with the reason. Observability beats post-hoc debugging every time.

## Tools

Node.js for the main pipeline orchestration. Python for analytics, the ML scoring model, and a small control layer. Claude API (Haiku + Sonnet, routed by task) for the AI layer, with tool-use for structured outputs. Apify and Clay for scraping and enrichment. Custom Python scrapers for niche sources. Airtable as the operational queue. PostgreSQL for the analytics warehouse. Pipedrive as the operational system destination. HeyReach for the cadence layer. GitHub Actions for scheduled runs and monthly retraining of the scoring model.
