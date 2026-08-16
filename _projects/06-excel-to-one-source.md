---
layout: project
title: From 11 Excel files to one source of truth
tagline: "A folder of monthly Excel files, different formats, broken headers, totals mixed into the rows. One automated flow reads them all, cleans them, and feeds one dashboard that updates itself."
description: "The most common small-business data problem: a folder of monthly Excel exports that nobody can add up. Different column names each month, headers split over two rows, and summary totals sitting in the middle of the data. This is how I turn that folder into one dashboard that updates itself, using Power Query folder ingestion, a clean model, and a small set of DAX measures."
tools: [Power BI, Power Query, DAX, Excel]
outcome_headline: "One folder in, one dashboard out, with no hand-editing of any file"
outcome_detail: "Drop next month's file into the folder and the dashboard updates on its own. No renamed columns to fix, no totals to delete by hand, no copy-paste. The rules that clean the files are written once and run every refresh."
order: 3
cover_image: /assets/images/projects/excel-to-one-source-cover.png
---

**This build is in progress.** The page documents the method and the dataset design. The dashboard screenshots follow when it ships.

Built in Power BI with Power Query and DAX. The source is a seeded synthetic generator that produces twelve months of deliberately messy Excel files.

Almost every small business I talk to has this folder. One file per month, exported from a system or typed by hand, sitting in SharePoint or on a shared drive. Each file is readable on its own. Together they are unusable, because no two months agree on what the columns are called or where the data starts. Somebody rebuilds the summary by hand every month, and that person is usually the owner.

The figures are synthetic, generated from a seeded script. The mess is modelled on what these folders actually look like. The method is the point.

## The business question

The owner's question is simple and nobody can answer it quickly: **what did we actually sell this year, by product and by customer, and how does this month compare to the same month last year?**

The data to answer it already exists. It is sitting in the folder. The reason nobody can answer is not analysis. It is that adding the files together takes a day of manual work, so it gets done rarely, late, and differently each time.

The real requirement is not a chart. It is that next month's file lands in the folder and the answer updates without anyone touching it.

## Where the data comes from

Twelve or more monthly workbooks in one folder, generated to carry the four failures these files always carry:

- **Headers split over two rows.** A merged title row on top, the real column names underneath. Excel exports do this constantly, and a naive import reads the title as the header and everything else as text.
- **Column names that drift.** `Customer` becomes `Customer Name` in March and `Cust.` in September. Positional imports break silently here: the data still loads, it just loads into the wrong column.
- **Summary rows inside the data.** A `Total` row at the bottom of each product group. Import it and every figure is counted twice.
- **Mixed types in one column.** Dates stored as text in some months, real dates in others. Amounts with a thousands separator in a few files, making the whole column text.

Each of these is the kind of thing that makes a hand-built consolidation quietly wrong rather than obviously broken. That is what makes it worth automating.

## The approach

Power Query reads the **folder**, not the files. That is the whole trick, and it is why the solution keeps working after handover.

A folder query lists every workbook in the directory. One sample file becomes a transformation function. That function runs against every file, current and future. Adding month thirteen means dropping the file in the folder. Nothing else changes.

The transformation steps, in order, and each one exists because of a specific failure above:

1. **Promote the real header row** by skipping to the first row that carries the expected column names, rather than assuming row one.
2. **Rename by lookup, not by position.** A small mapping table translates every known variant (`Cust.`, `Customer Name`) to one canonical name. An unrecognised column raises an error instead of loading into the wrong place.
3. **Remove summary rows** by filtering out rows where the key columns are blank or the label matches a total pattern, before anything is added up.
4. **Set types explicitly** on every column, with locale set, so a text date or a separated number fails loudly at load rather than silently later.
5. **Add the source file name and month** as columns, so any number on the dashboard can be traced back to the file it came from.

Step 2 is the one that matters most and gets skipped most often. Renaming columns by position is the single most common way one of these consolidations goes wrong, because it never throws an error.

## The data model

The cleaned output becomes a fact table at one row per invoice line, with dimensions for date, product, and customer. A star, not a flat sheet.

That shape is what makes the "same month last year" comparison a one-line measure instead of a manual lookup. It also means the model stays correct when a new product or a new customer appears, because they arrive as new rows in a dimension rather than new columns in a sheet.

A proper date table, marked as the date table, carries the calendar. Time comparisons do not work reliably without one.

## Cleaning and validation

The consolidation is only worth having if it is provably right, so the checks are part of the build, not a one-off review:

- **Row count reconciliation.** Rows loaded per file against rows in the file, so a silently dropped month is visible.
- **Total reconciliation.** The sum per month against the summary row that was deliberately removed, since that total was the file's own claim about itself. They must agree.
- **A blank-key check** that fails the refresh if a row arrives with no product or no customer.

The removed total rows are the cheapest validation available here. They were the problem during import and they are the answer key afterwards.

## The deliverable

One Power BI report on a scheduled refresh, and a small set of DAX measures:

- Revenue, cost, and margin
- The same three for the prior year, over the marked date table
- Variance and variance percent, using `DIVIDE` so a missing prior year returns blank instead of an error

The pages answer the owner's question directly: total by month against last year, revenue and margin by product, revenue by customer, and a table that traces any figure back to its source file.

The handover is the folder rule: **drop the file in, the dashboard updates.** No document explaining which columns to rename first.

## What I'd do differently

The mapping table in step 2 is a maintenance cost, and it should live in a small Excel file the client owns rather than inside the query. When a new column variant appears, the person who sees it first should be able to add a row without opening Power BI. Burying that mapping in the query is a decision that looks tidy on build day and turns into a support call six months later.

The other thing to watch: this method works because the files, however messy, are exports of the same underlying thing. If the folder holds genuinely different reports, folder ingestion is the wrong tool and the honest answer is to fix the export rather than automate around it. Automating a consolidation that should not exist is a way of making a bad process permanent.

## Tools, by step

| Step | Tool | What it does here |
|---|---|---|
| Source | A folder of monthly Excel workbooks (synthetic, from a seeded generator) | Twelve months of the four failures above, reproducible from scratch |
| Ingestion | Power Query folder query plus a sample-file function | Reads every file in the folder, current and future, with one set of rules |
| Cleaning | Power Query, named steps | Header promotion, rename by lookup, total-row removal, explicit types, source-file tagging |
| Model | Power BI, star schema with a marked date table | One row per invoice line, dimensions for date, product, customer |
| Measures | DAX | Revenue, cost, margin, prior year, variance, all over the marked date table |
| Refresh | Power BI scheduled refresh | New file in the folder, dashboard updated, nobody retypes anything |
