---
layout: project
title: "Power BI, SQL and data analytics at a seed company"
tagline: "Excel and the accounting export go into one Azure SQL database with the business rules in SQL, and Power BI reports from it."
description: "How I built the data foundation and the Power BI reporting at Veginova, a family-owned seed company: Excel on SharePoint and the accounting export into Azure SQL, a Python load service, two semantic models and four reports. Three revenue numbers became one, and the production plan matches the planner's own spreadsheet."
tools: [Power BI, DAX, Power Query, Azure SQL, T-SQL, Python, Azure Functions]
facts:
  role: "Built on my own at Veginova, my family's seed company, as Data Analyst and then Power BI & Power Apps Developer"
  when: "2025 to 2026"
  stack: "Power BI, DAX, Power Query, Azure SQL, T-SQL, Python, Azure Functions, Logic Apps"
  result: "Three revenue numbers became one, tied to the official accounts. The production plan matches the planner's own spreadsheet with zero mismatches."
outcome_headline: "Three revenue numbers became one, tied to the official accounts."
outcome_detail: "The production plan matches the planner's own spreadsheet with zero mismatches."
featured: true
order: 1
cover_emoji: "3 → 1"
coming_soon: false
redirect_from:
  - /projects/03-veginova-operations/
  - /projects/04-veginova-invoices/
  - /projects/06-excel-to-one-source/
---

Veginova is a family-owned seed company in Odense. It's my family's company, and I work there.

I built its data foundation and its reporting on my own: Excel on SharePoint and the accounting export load into one Azure SQL database, the business rules live in T-SQL, and Power BI reports from it. Three revenue numbers became one, tied to the official accounts. The production plan matches the planner's own spreadsheet with zero mismatches.

The company's revenue, customers and prices stay private, so this page shows a diagram of the system and no report screenshots.

## The problem

The numbers lived in Excel workbooks and in the accounting system, and they didn't agree. There were three revenue numbers, so nobody could act on any of them.

The production plan lived in a spreadsheet the planner kept by hand. It was out of date as soon as a sale landed or stock changed, and that matters in this business because seed takes about a year to grow. A shortage found late can't be fixed that season.

## What I built

<figure class="arch-diagram">
<div class="arch-flow">
<div class="arch-box"><em>Sources</em><b>Excel and accounting</b><small>Locked Excel workbooks on SharePoint and the ledger export from the accounting system</small></div>
<div class="arch-box"><em>Load</em><b>Python load service</b><small>Azure Function and Logic App, every ten minutes in the working day. Failed rows go to quarantine</small></div>
<div class="arch-box arch-box--focus"><em>Database</em><b>Azure SQL</b><small>A test copy and a live copy. Business rules in T-SQL, built from numbered migrations</small></div>
<div class="arch-box arch-box--focus"><em>Reporting</em><b>Power BI</b><small>Two semantic models and four reports. Daily reports kept apart from analysis reports</small></div>
</div>
<div class="arch-side"><b>Also on the database: Power Apps and Claude</b><small>The operations app and the AI layer are on the Power Platform and AI page.</small></div>
<figcaption>The system at Veginova, drawn as a diagram. The green boxes are what this page covers.</figcaption>
</figure>

### Sources

People keep working in Excel. Four locked workbooks on SharePoint hold the forecast, the stock, the manual finance entries and the master data, and the accounting system delivers its ledger export.

### Load service

A Python service runs in an Azure Function every ten minutes during the working day. It reads the files through a Logic App and loads rows only through stored procedures. A row that fails a check is parked in a quarantine table and I get an email, so a bad row never reaches a report and never disappears either.

### Database

Azure SQL, with a test copy and a live copy. It has layers for staging, reference data, core tables, operations marts, finance marts and audit. The live copy held 443 database objects on 19 November 2026, built from 111 numbered migration files. All business rules are in SQL, so every report and every app reads the same answer.

### Production planning in SQL

The production need per variety is safety stock plus expected sales, minus stock and incoming seed, and never below zero. It's the planner's own calculation, moved into a view that recalculates when sales or stock change.

### Power BI

Two semantic models, one for finance and one for operations, with 84 measures in the catalog. Four reports with 13 pages sit on top. The daily operational reports are kept apart from the analysis reports, because a person checking today's orders and a person studying a season need different pages. The reports are PBIP projects in git, and a lint script checks them before a publish.

### The move to Azure SQL

The first version ran on Postgres (Supabase). I prototyped Microsoft Fabric and dropped it on cost, because a Fabric capacity added no function the company needed at its size. I moved the system to Azure SQL in August 2026. All 17 tables were copied with exact row counts, and revenue reconciled with no difference.

## How it is checked

- Every change is built in the test copy first, and the scripts point at test unless I say otherwise.
- Revenue totals are reconciled to the audited accounts on every change. If the total moves, the change stops.
- The production plan is compared with the planner's spreadsheet, variety by variety.
- A spot check traces single records from the source file to the report page.
- Each release has a written check record. I read every line that isn't a pass and sign it, and my signature is the release.

## The result

- Three revenue numbers became one, tied to the official accounts.
- The production plan matches the planner's own spreadsheet with zero mismatches.
- The load runs on a schedule. It refreshes itself every ten minutes during the working day.

I tested a statistical forecast against the sales history and refused it, because demand at a seed company is intermittent and the model would have produced noise. The plan uses the planner's expected sales as input.

## Built, not yet in daily use

- A forecast range per variety and season, with a low, a base and a high figure calculated in SQL and versions that are approved and frozen. It's built, and the planner doesn't work from it yet.
- The integration that reads from and books into the accounting system. It's built and tested in the test copy, and it waits on credentials and the bookkeeper's approval.

## What I bring to a contract

- Power BI end to end: the semantic model, DAX, Power Query, report design and the publish.
- The database behind the reports: Azure SQL, T-SQL, numbered migrations, and a test copy before live.
- Python loads on a schedule in Azure Functions, with a quarantine for rows that fail.
- A number check on every change, so your finance people see the same total in the report as in the accounts.
- I work by the hour on longer engagements, inside your team or as the one person who builds it all.

The app and the AI layer on the same database: [Power Platform and AI development at a seed company]({{ '/projects/veginova-power-platform-ai/' | relative_url }}).
