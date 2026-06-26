---
layout: project
title: Operations & Production Planning
tagline: "A live system that tells a seed business what to produce, how much, and when — reproducing the planner's own numbers exactly, 22 of 22 varieties. A planning system with scenario testing, not a forecast."
description: "Production planning ran on a spreadsheet that went stale the moment a sale landed — dangerous when seed takes a year to grow. I rebuilt the planner's logic as a live system that reproduced his existing numbers exactly (22 of 22 varieties), flags shortages before the year-long lead time makes them unfixable, and tests scenarios before seed is committed."
tools: [Python, PostgreSQL, Supabase, Power BI]
outcome_headline: "Reproduced the planner's existing production numbers exactly — 22 of 22 varieties tied — then made the plan live, forward-looking, and testable"
outcome_detail: "The model matched the hand-built spreadsheet on every variety. It computes what to produce from live sales, stock, and incoming orders, flags shortages early enough to act on a one-year production lead time, and lets the planner pressure-test a big sale or a capacity drop before committing seed."
order: 2
cover_image: /assets/images/projects/veginova-operations.jpg
coming_soon: true
---

Built for Veginova, a seed business with a hard constraint: seed takes about a year to produce. The validation in this piece — that the system reproduced the planner's own numbers on 22 of 22 varieties — is real. Where I quote how many varieties were at risk or how much to produce, those figures are **illustrative**: the shape of the real plan with the confidential client numbers replaced. The system, and the validation that proves it works, are the real ones.

## The problem

At Veginova, production planning ran on a spreadsheet the planner maintained by hand. It worked — until it didn't. The moment a sale landed or stock changed, the spreadsheet was out of date, and the production decisions built on it were based on stale numbers.

The stakes are high because of one brutal fact: **seed production takes about a year.** If you discover you're short of a variety, it's already twelve months too late to make more. You can't react to a stockout — you have to see it coming.

The planner was effectively running the whole production–inventory–sales triangle in his head:

- How much will we sell of each variety?
- How much do we have, and how much is arriving?
- So how much must we produce — and when do we have to start?

Get it wrong in either direction and it costs real money: produce too little and you miss a year of sales you can't recover; produce too much and you tie up cash in seed you don't need.

## What I did

I took the logic the planner was running by hand and built it into a live system. For every seed variety, it computes the core question — **how much to produce** — from what's actually selling, what's in stock, and what's already on the way.

Three things made it useful beyond the spreadsheet:

- **It stays current.** When sales or stock change, the plan updates — no manual rebuild.
- **It respects the one-year lead time.** It flags which varieties are short, and *when* production has to start to cover each one in time.
- **It tests scenarios.** The planner can ask "what if sales come in higher," "what if production capacity drops," or "what if we lose stock" — and see which varieties go at risk.

## What I found — and how I proved it

The real test of a planning system is whether it matches reality. I validated the model against the planner's own existing spreadsheet — the numbers he'd built by hand over years of running the business.

**It reproduced his planning figures exactly — 22 of 22 varieties matched, zero mismatches.** That's what made it trustworthy: it wasn't a different answer, it was *his* answer, made live and able to update itself. A planner doesn't adopt a system that argues with him; he adopts one that agrees with him and then keeps up.

<!-- SCREENSHOT NEEDED: Operations — Production page (red/green status per variety, produce quantities) -->
![Operations dashboard — production plan with red/green status per variety]({{ '/assets/images/projects/veginova-operations-production.png' | relative_url }})
*The production plan: each variety flagged red or green against its safety line, with the quantity to produce. The planner's red/green sheet, made live and always current.*

The system surfaced what the spreadsheet couldn't show at a glance:

- **A handful of varieties were sitting below their safety line** and would run short within the planning window. <!-- PLACEHOLDER: illustrative — replace with the real count of at-risk varieties -->
- **Several varieties needed production this cycle**, with the quantity and timing to cover demand before the lead time closed the window. <!-- PLACEHOLDER: illustrative — replace with real produce count / quantity -->
- A clear view of which varieties to produce, in which location and cycle, and how much.

<!-- SCREENSHOT NEEDED: Operations — Need vs Plan comparison (computed need beside the planner's target) -->
![Need versus plan — computed production need beside the planner's target]({{ '/assets/images/projects/veginova-operations-need-vs-plan.png' | relative_url }})
*Computed need beside the planner's own production target, variety by variety — so the gap between "just enough" and "his batch size" is visible, not buried.*

## The business impact

- **Production decisions from live data, not a stale spreadsheet.** The plan shows what's actually happening, not last month's snapshot.
- **Stockouts visible before they're unfixable.** With a one-year lead time, seeing a shortage early is the entire game — it's the difference between covering it and missing a year of sales.
- **The manual spreadsheet work each planning cycle largely disappears** — the system maintains the plan that used to be rebuilt by hand. <!-- PLACEHOLDER: illustrative time-saving — replace with the real before/after if quoting one -->
- **Scenario testing** lets the planner pressure-test a decision — a big order, a capacity problem, a stock loss — before committing seed to a year in the ground.

## What the business does now

The planner runs production off a system that updates itself and shows what's at risk before it's too late to act. He can commit production decisions with confidence, see months ahead which varieties will run short, and test the impact of a big sale or a capacity problem before it happens — instead of finding out a year later. <!-- PLACEHOLDER: confirm/replace with the real recommendation and any specific varieties/figures before publishing -->

**An honest note on what this is.** This is a planning system with scenario testing, validated against ground truth. It is **not** statistical forecasting — and that distinction matters. The business runs on named deals, not predictable trends, so the planner's judgment is the input; the system makes that judgment live, fast, and forward-looking. Claiming a forecast the data can't support would be the weaker move. Reproducing the planner's own numbers on every variety, and turning them into something that updates itself and looks a year ahead, is the stronger one — and it's the true one.
