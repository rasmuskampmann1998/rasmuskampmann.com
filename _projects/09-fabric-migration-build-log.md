---
layout: project
title: "Consolidating a Seed Company onto Microsoft Fabric"
tagline: "Build log, in progress: moving Veginova's data platform onto Microsoft Fabric. One platform for ingestion, modelling, and reporting, with Claude in the pipeline where the data has no structure. Updated as pieces ship."
description: "An ongoing build log: consolidating Veginova's reporting stack onto Microsoft Fabric. Fabric SQL Database, a Direct Lake semantic model on OneLake, Power BI on top, Excel-native inputs on SharePoint, Claude API invoice extraction with human approval, Power Automate for event-driven file sync."
tools: [Microsoft Fabric, Power BI, T-SQL, Python, Claude API, Power Automate]
outcome_headline: "Ongoing build, not a finished case"
outcome_detail: "The sales dashboard is the first artefact due on the new platform, planned for mid-August. This page states what is built or in progress, nothing more, and is updated as pieces ship."
order: 3
cover_emoji: "🏗️"
coming_soon: false
---

**This is a build log, not a finished case study.** The work is ongoing at Veginova. What's below is built or actively in progress, and the page gets updated as pieces ship, starting with the sales dashboard in mid-August.

**Pillars this case proves:** data depth · AI fluency · close to the decision makers

## Why Fabric at this company size

A company this size doesn't need a big-data platform, and pretending otherwise is how over-dimensioning happens. Fabric won on two things: consolidation and native write-back.

Consolidation first. The earlier builds ran on a Postgres instance, Python loaders, and Power BI stitched together. It worked, and the finance and operations dashboards on this site came out of it. But every seam is a thing to maintain. Fabric puts ingestion, storage, the semantic model, and reporting in one platform with one security model.

Write-back second. The approval steps in the pipeline need a supported way to write a human decision back into the database. Fabric has one. The stitched-together stack never did.

The trade-off is real: Fabric is more platform than the company strictly needs today. The hedge is portability. The business logic lives in T-SQL and Python, and both move if the platform choice ever has to be revisited.

## The architecture

The core, in order:

- **Fabric SQL Database** is the operational store. Staging tables, the dimensional model, and the reconcile checks live here in T-SQL.
- **OneLake with a Direct Lake semantic model.** The database mirrors into OneLake automatically and the semantic model reads it there. No import refresh to schedule and no refresh window to miss.
- **Power BI** renders on top. Same rule as the earlier builds: logic upstream, thin measures.

Around the core:

- **Excel-native inputs on SharePoint.** The team works in Excel, so the platform meets them there. A file saved to SharePoint flows into the pipeline on its own.
- **Power Automate** handles the event-driven file sync: a saved file is a triggered pipeline. Nobody runs an import.
- **Claude API invoice extraction.** Invoice line items are extracted by Claude with a confidence score per field. Low-confidence rows route to a human approval step built as a translytical task flow, a Power BI feature that writes the approval back into the database from the report. Nothing lands unreviewed.

## Status

Ongoing. The first artefact due on the new platform is the sales dashboard, planned for mid-August. This page is updated when it ships.
