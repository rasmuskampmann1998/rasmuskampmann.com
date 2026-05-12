---
layout: project
title: Market Intelligence Platform
tagline: "Real-time competitive and market intelligence: ~800 sources, hundreds of articles interpreted daily, with agentic scraping and semantic search"
tools: [FastAPI, Python, Supabase, pgvector, Apify, APScheduler, Docker, Claude, React]
outcome_headline: "Replaces a daily manual briefing with a continuously updated dashboard, RAG-powered chat, and weekly auto-generated PDF"
outcome_detail: "Agentic scrapers, multi-LLM routing, SQL migrations, semantic search, cron-based ETL. Live at tomato-intel-api.onrender.com."
order: 7
cover_image: /assets/images/projects/tomato-intel.jpg
github_url: https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies/tree/main/07-tomato-intel
---

## Live demo

[tomato-intel-api.onrender.com](https://tomato-intel-api.onrender.com)

## The question

An agricultural technology client needed continuous visibility across a fragmented intelligence landscape. Crop prices, regulatory changes across 27 countries, competitor product launches, patent filings, news in three languages, social signals. Manual monitoring was a full-time job that produced incomplete, stale briefings. Could I replace the manual work with a platform that collects, interprets, and surfaces only what's relevant?

## What the platform does

A full-stack market intelligence system covering the full pipeline from raw scrape to executive briefing.

- **Agentic scraping.** A Claude-driven agent decides which source to pull from next, plans the scrape sequence, and routes around failures using a small tool set (run an Apify actor, fetch a URL, parse an article, write to the warehouse, flag a broken source). The model picks the right tool for the source on its own.
- **Web scraping at scale.** Around 800 sources across LinkedIn, Twitter, Reddit, Google News, Jobindex, Meta Ads Library, Trustpilot, price feeds, regulatory portals. A mix of Apify actors and custom Python (trafilatura, Playwright, selectolax).
- **ETL pipeline.** Raw scrape rows land in a Supabase staging table. A typed transform step writes them into the canonical intelligence schema, with consistent country codes, source IDs, and timestamps. Idempotent on a content hash.
- **SQL warehouse with migrations.** PostgreSQL on Supabase, schema versioned with timestamped migration files. Every schema change is reviewable and reproducible.
- **Cron-based automation.** APScheduler runs inside the FastAPI process. Different jobs on different cadences: hourly for price feeds, every four hours for news, daily for jobs and social, weekly for the briefing PDF.
- **REST API.** FastAPI exposes endpoints for the dashboard, briefings, source-health, and a chat endpoint that wraps an LLM with retrieval.
- **LLM interpretation.** Each incoming article gets read by Claude, classified by topic and region, summarised in plain language, and scored for relevance against the client's strategic priorities.
- **Multi-LLM routing.** Different prompts route to different model families. Cheaper Haiku-tier models handle bulk classification and translation. Sonnet-tier models handle cross-source reasoning. A single routing layer handles fallbacks.
- **RAG with semantic search.** All interpreted articles are embedded into a `pgvector` table on Supabase. The dashboard's chat panel lets the user ask questions like "what's been happening with seed prices in Spain this month?" and the answer is composed from the top-k retrieved articles, with sources cited inline.
- **Frontend and PDF export.** React frontend deployed on the same Render service as the API. A weekly PDF compiles the top stories of the week and ships to leadership on Monday morning.

## How the agentic scraper works

A traditional scraper is scripted: it runs a fixed sequence and breaks when a source changes layout.

The agentic version takes a goal ("get the latest seed-price news for Spain") and decides itself which source to query, how to parse it, and what to do if a source fails. The agent has a small toolset:

- `apify_actor.run(actor_id, input)` runs a pre-built Apify scraper
- `http_get(url)` fetches a URL with sensible defaults
- `parse_article(html)` extracts the main article body
- `store(record)` writes a typed row to the warehouse
- `mark_source_failed(source_id, reason)` flags the source as needing manual attention

The model plans the sequence, executes it through tool calls, and routes around failures. The pattern uses Claude's tool-use API directly with structured JSON tool definitions.

## Schema migrations

Eight versioned migration files cover the full evolution of the warehouse:

- Core tables for sources, raw scrapes, and articles
- `pgvector` extension for embeddings
- Per-run scrape logging for the Scrape Status panel
- Translation table for multi-language sources
- Chat history persistence for the RAG panel
- Company-aggregation layer that joins articles to tracked competitors

Migrations are applied through a small Python harness that records the latest version in a `schema_migrations` table. Every change is reviewable in the repo.

## What it surfaces

A typical week:

- A regulatory change in one EU country that's about to apply bloc-wide
- A competitor launching a product in a region, picked up from a local trade-press article plus a job posting on their careers page
- A price movement that breaks a recent trend, with the article that caused it linked underneath
- A semantic-search query like "patent activity around drought-tolerant tomato varieties" returning a ranked list of articles with one-paragraph summaries

The job that used to take a person most of a week now takes the system a few hours of compute and surfaces more than the manual version did.

## Tools

FastAPI for the backend, Docker for portability. Supabase (PostgreSQL with `pgvector`) for the warehouse and embeddings. APScheduler for the cron layer. Apify and custom Python scrapers for data collection. Claude (Haiku and Sonnet, routed by task) for interpretation and the agentic loop. React on the frontend. Sentry and structured logging for observability.
