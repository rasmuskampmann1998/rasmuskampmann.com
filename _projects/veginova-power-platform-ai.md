---
layout: project
title: "Power Platform and AI development at a seed company"
tagline: "A Power Apps operations app on Azure SQL for orders, invoices, stock and quality tests, built with Claude Code and released on my sign-off."
description: "How I built the Power Apps operations app at Veginova, a family-owned seed company: nine screens on Azure SQL, generated from Python, with lot traceability, a quality gate and permissions in the database. Built with Claude Code in VS Code and GitHub, and every release is signed off by me."
tools: [Power Apps, Power Automate, Azure SQL, T-SQL, Python, Claude Code, MCP]
facts:
  role: "Built on my own at Veginova, my family's seed company, as Power BI & Power Apps Developer"
  when: "2026"
  stack: "Power Apps, Power Automate, Azure SQL, T-SQL, Entra ID, Python, Claude Code, VS Code, GitHub, MCP"
  result: "A lot can only be sold once its quality test releases it. Stock is calculated from every movement since the last count, lot by lot."
outcome_headline: "A lot can only be sold once its quality test releases it."
outcome_detail: "Stock is calculated from every movement since the last count, lot by lot."
featured: true
order: 2
cover_emoji: "9 screens"
coming_soon: false
---

Veginova is a family-owned seed company in Odense. It's my family's company, and I work there.

I built its operations app on my own: a Power Apps canvas app with nine screens on an Azure SQL database, generated from Python, with the rules and the permissions in T-SQL. A lot can only be sold once its quality test releases it. Stock is calculated from every movement since the last count, lot by lot. I build with Claude Code in VS Code and GitHub, and I sign off every release.

The company's customers, prices and stock figures stay private, so this page shows a diagram of the system and no app screenshots.

## The problem

The daily work ran in Excel. Stock, the forecast, the manual finance entries and the master data each had a workbook, and three product lists disagreed.

A spreadsheet takes any entry. It couldn't hold a rule such as selling only from a lot whose quality test has passed, and it couldn't show which movements a stock figure was built from.

Seed is sold by lot, so the company needs to trace each lot from its test to the order it went on.

## What I built

<figure class="arch-diagram">
<div class="arch-flow">
<div class="arch-box"><em>Sources</em><b>Excel and accounting</b><small>Excel stays the front door for the lists people already keep</small></div>
<div class="arch-box"><em>Load</em><b>Python load service</b><small>Loads the files into the database every ten minutes in the working day</small></div>
<div class="arch-box arch-box--focus"><em>Database</em><b>Azure SQL</b><small>Lot ledger, quality gate, approvals and permissions, all in T-SQL. Sign-in through Entra ID</small></div>
<div class="arch-box arch-box--focus"><em>App</em><b>Power Apps</b><small>Nine screens, generated from Python. The same build goes to test, then live</small></div>
</div>
<div class="arch-side"><b>Beside the database: Claude through MCP</b><small>Claude reads and proposes, and a person approves. Set up, not in daily use. Power BI reports from the same database.</small></div>
<figcaption>The system at Veginova, drawn as a diagram. The green boxes are what this page covers.</figcaption>
</figure>

### The operations app

A Power Apps canvas app on the live database, with nine screens: today, sales, stock, finance, plan, tasks, analysis, settings and breeding. It works in three languages.

The app covers sales orders, invoices and credit notes with a PDF, stock movements and stock counts, germination tests, payments and reminders, month-end close and tasks. A person does each of these in one place, and the database checks the entry before it's stored.

### Generated from Python

I never edit the app by hand. About 9,800 lines of Python generate it, so every screen follows the same pattern and a change is a code change in git. The same build goes to the test copy first and then to live, and a compare step has to report the two as identical before I release.

### Lot traceability and the quality gate

Every lot has a ledger. Stock is calculated from every movement since the last count, lot by lot, and each lot carries its thousand-seed weight, germination percent, quantity, status and retest date.

A lot can only be sold once its quality test releases it. The minimum germination per species comes from EU Directive 2002/55/EC, and a lot is retested every 12 months. The gate is a rule in the database, so the app can't skip it.

### Permissions in the database

Each person signs in to SQL as themselves through Entra ID, and the approval rules sit in the stored procedures. Write-offs and corrections wait for a named person to approve them. Invoices run in a gapless series, and eight core tables have an audit trail.

I put the permissions in the database rather than in the app, because an app screen can be bypassed and a stored procedure can't.

## How I work with AI

I work agentic. I build with Claude Code in VS Code and GitHub, and Claude drafts SQL, Python and app screens from written procedures. I have 21 of them, one for each kind of work.

Review agents read the draft for number, SQL, Python, Power BI and security errors. Scripts carry more weight than the agents, because a script that compared two builds once found two bugs that seven review agents had missed.

AI calculates no number in the system. The numbers come from SQL, and I refused a text-to-SQL chatbot for that reason.

## How it is checked

- Every change is built in the test copy first, and the same build goes to live.
- Every write to the database goes through a tested script: back up, a small batch, a check, then the rest.
- Totals are reconciled to the audited accounts on every change.
- Each release has a written check record. I read every line that isn't a pass and sign it, and my signature is the release.

## The result

- A lot can only be sold once its quality test releases it.
- Stock is calculated from every movement since the last count, lot by lot.
- Orders, invoices, credit notes, stock, germination tests, payments and month-end close are in one app with nine screens, on one database.

## Built, not yet in daily use

- Claude connected to the database through MCP. It answers questions on the plan and proposes changes, and a person approves every change. I set it up on my planning demo, which runs the same design on synthetic data. It's not in daily use at Veginova.
- Photo reading. Claude is set up to read photos of seed packets, sowing plans and bills into rows, and a person confirms every row. It never writes stock or invoices.
- A phone scan app with five screens for seed packets, sowing plans, stock counts and bills. It was published in November 2026, and the staff don't use it daily yet.
- The accounting integration. It's built and tested in the test copy, and it waits on credentials and the bookkeeper's approval.

## What I bring to a contract

- Power Apps canvas apps on Azure SQL, with Power Automate and SharePoint where they fit.
- Business rules and permissions in the database, so the app stays thin and the rules hold for every tool that connects.
- A test copy and a live copy, the same build to both, and a written check before each release.
- Agentic development with Claude Code, with a person accountable for every release. On your contract that person is me.
- I work by the hour on longer engagements, inside your team or as the one person who builds it all.

The data foundation and the reports on the same database: [Power BI, SQL and data analytics at a seed company]({{ '/projects/veginova-power-bi/' | relative_url }}).
