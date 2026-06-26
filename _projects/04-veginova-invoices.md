---
layout: project
title: Invoice & Financial Dashboard
tagline: "One trusted view of profit per product, profit per customer, and the cash owed — built from invoices, reconciled to the accounts within 1.25%. Commercial figures below are illustrative; the reconciliation is real."
description: "A seed business had two sets of numbers that disagreed: tax accounts that hid the commercial picture, and invoices that held the truth. I made the invoices the source, reconciled them to the official 2024 revenue within 1.25%, and put profit per product, profit per customer, and accounts receivable on one trusted view."
tools: [Python, PostgreSQL, Supabase, Power BI]
outcome_headline: "Reconciled three conflicting revenue numbers to one trusted figure, then made profit visible per product and per customer for the first time"
outcome_detail: "2024 revenue tied to the official accounts within 1.25%, the gap fully explained by currency timing. With the numbers trusted, gross margin per seed variety, customer profitability, and accounts receivable became visible on a single live view."
order: 1
cover_image: /assets/images/projects/veginova-invoices.jpg
coming_soon: true
---

Built for Veginova, a seed business selling tomato, pepper, and nightshade varieties across Europe and the Middle East. The reconciliation figures in this piece (the 2024 revenue match, the 1.25% tolerance) are real. The commercial detail — per-product margins, customer profitability, receivables amounts — is **illustrative**: the shape and scale of the real findings, with the confidential client figures replaced. The method, and the result that mattered, are the real ones.

## The problem

Like many small businesses, Veginova's numbers lived in two places that didn't agree. The official accounts were structured for tax — which meant they *hid* the real commercial picture: which products actually made money, which customers were worth keeping, and how much cash was tied up in unpaid invoices.

Leadership couldn't answer basic commercial questions with confidence:

- What's the real gross margin on each seed variety?
- Which customers drive profit, and which just drive volume?
- How much money is owed to us right now, and when will it arrive?

The accounts said one thing. The invoices said another. Nobody could trust a single number — and you can't make a commercial decision on a number you don't trust. That distrust is common at this level: in a 2024 survey of more than 1,300 finance leaders, nearly 40% said they don't fully trust their own organisation's financial data. Veginova was living that problem.

## What I did

I made one decision that shaped everything: **the invoices are the truth.** They're the record of what was actually sold, to whom, at what price. The tax accounts became a cross-check, not the source.

Then I built one connected system that:

- Pulled every invoice down to the line item — product, customer, price, cost
- **Reconciled the invoice revenue against the official accounts** to prove the numbers tied out
- Calculated gross margin per seed variety and profit per customer
- Tracked accounts receivable — what's owed, how old it is, when it's expected

All of it on a single source of truth, refreshed from the company's own files. There's a deliberate limit here, and it's an honest one: the dashboard measures **contribution margin** — revenue minus the direct cost of the seed — not bottom-line profit. Overhead lives in the bookkeeping system, and rebuilding it here would just duplicate the official accounts. So the margins below are contribution, the number that tells you which products carry the business, not statutory profit.

## What I found

The reconciliation held: **2024 revenue tied to the official figure of 2,312,690 DKK, within 1.25%** — and the remaining gap was fully explained by currency timing, not error. That match is the whole foundation. It's the difference between "here's a number" and "here's a number you can act on," and it's the first thing a finance reader should be told: it ties out, and the proof is one click away.

With trustworthy numbers, the commercial picture finally became visible:

- **Gross margin per product** — the seed lines spread far wider than leadership assumed. The top varieties carried a contribution margin around 90%, while a handful of lines sat closer to 60% once their real cost was attributed. <!-- PLACEHOLDER: illustrative — replace with real per-variety margin spread before treating as factual -->
- **Customer profitability** — roughly a fifth of customers generated about three-quarters of the contribution. <!-- PLACEHOLDER: illustrative — replace with real customer-concentration figures -->
- **Accounts receivable** — around 1.2M DKK was outstanding, of which roughly a quarter had aged past 90 days and was quietly at risk. <!-- PLACEHOLDER: illustrative — replace with real AR total and ageing split -->

<!-- SCREENSHOT NEEDED: Finance — Overview / P&L Revenue page (revenue, contribution margin, AR at a glance) -->
![Finance dashboard — revenue, contribution margin, and receivables on one view]({{ '/assets/images/projects/veginova-finance-overview.png' | relative_url }})
*The overview page: revenue, contribution margin, and accounts receivable on a single trusted view. The reconciliation result sits behind the revenue figure — leadership is told it ties out; the detail is one click down.*

## The business impact

- **One number instead of three.** Leadership stopped second-guessing the figures and started deciding from them — the single biggest change, and the one that made everything else usable.
- **Reporting that used to take the better part of a day each month now refreshes on its own.** <!-- PLACEHOLDER: illustrative time-saving — replace with the real before/after -->
- **Profit visible per product and per customer for the first time** — the data needed to decide what to grow, what to drop, and who to keep.
- **Receivables made visible** surfaced overdue invoices that had been sitting unchased — cash the business was owed but couldn't see. <!-- PLACEHOLDER: illustrative — replace with real recovered/flagged AR figure if quoting one -->

<!-- SCREENSHOT NEEDED: Finance — Receivables (AR) ageing page -->
![Receivables ageing — what's owed, how old, and what's at risk]({{ '/assets/images/projects/veginova-finance-receivables.png' | relative_url }})
*Accounts receivable by age. What used to require manual cross-referencing across spreadsheets is now a glance: what's owed, how old it is, and what's slipping past 90 days.*

## What the business does now

Leadership can answer the questions that were guesswork before: which varieties to push, which customers to prioritise, and where the cash is.

The recommendation that came out of it: **concentrate commercial effort where the contribution is** — push the high-margin varieties, protect the small group of customers driving most of the profit, and tighten collection on the invoices aged past 90 days, where the cash is most at risk. <!-- PLACEHOLDER: confirm/replace with the real recommendation and the specific varieties/customers/figures before publishing --> None of those calls were possible while the numbers were in dispute. The dashboard didn't just report the business — it settled which number was real, and that's what turned reporting into decisions.
