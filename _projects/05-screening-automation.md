---
layout: project
title: Candidate Screening Automation
tagline: "7 data sources → structured PDF screening report in 8 minutes, fully automated"
tools: [Node.js, Claude API, Apify, Google OSINT, n8n, Airtable]
outcome_headline: "Cuts initial candidate screening from 2 hours to 8 minutes"
outcome_detail: "Consistency score, social media red flags, and executive summary — generated before the first interview."
order: 5
cover_emoji: "🔍"
---

## The Problem

Senior hiring managers were spending 2+ hours on initial candidate research before first-round interviews — checking LinkedIn, Googling names, cross-referencing CVs, scanning social profiles. The work was repetitive but high-stakes: a missed inconsistency or a problematic social post had real downstream costs.

The goal was to automate the research phase entirely and deliver a structured report to the hiring team before each interview.

## Pipeline Architecture

Seven data sources are queried for each candidate, then three parallel Claude Haiku calls produce structured JSON outputs that are assembled into an HTML report.

<div class="arch-diagram">
Input:  name, email, LinkedIn URL, position, CV text (from form)
  │
  ├─ P1  LinkedIn Profile Scrape    →  current role, history, education (Apify)
  ├─ P2  Google OSINT               →  news, press, legal, GitHub mentions
  ├─ P3  Social Media Scan          →  Facebook, Instagram, Twitter posts
  ├─ P4  CV Parse                   →  structured jobs, education, skills
  │
  └─ P5  AI Analysis (3× Claude)
        ├─ Analysis 1: CV vs LinkedIn cross-reference → consistency score 0–100
        ├─ Analysis 2: Social media red flag scan → flag list + severity
        └─ Analysis 3: Executive summary → recommendation + key concerns
  │
  ├─ P6  HTML Report Generation
  ├─ P7  Airtable Log               →  SCREENING_LOG table
  └─ Output: structured report to hiring manager
</div>

## The AI Analysis Layer

Three sequential Claude Haiku calls handle different aspects of the evaluation. Each call returns structured JSON — no free-text parsing required:

```javascript
// Sanitised from analysis_prompts.js — Analysis 1: CV vs LinkedIn consistency

const analysis1Raw = await callClaude(
  `You are a thorough HR analyst. Compare CV data against LinkedIn for consistency.
   Output ONLY valid JSON — no markdown, no explanation.`,

  `CV Jobs:        ${JSON.stringify(candidate.cv_jobs)}
   LinkedIn Jobs:  ${JSON.stringify(candidate.li_positions)}
   CV Education:   ${JSON.stringify(candidate.cv_education)}
   LinkedIn Edu:   ${JSON.stringify(candidate.li_education)}

   Return this JSON:
   {
     "consistency_score": 0-100,
     "current_role_match": "match|mismatch|unverifiable",
     "job_discrepancies": [
       {"field": "", "cv_value": "", "linkedin_value": "",
        "severity": "minor|major", "explanation": ""}
     ],
     "unexplained_gaps": [{"period": "YYYY-MM to YYYY-MM", "duration_months": 0}],
     "inflated_titles": [{"cv_claim": "", "assessment": "", "severity": "low|medium|high"}],
     "summary": "2-3 sentence summary of findings"
   }`,
  1500
);
```

The second call scans social media posts for red flags (extreme views, aggression, professional misconduct signals). The third produces an executive summary with a structured hire/no-hire recommendation.

## Google OSINT

A structured search query set covers six categories of publicly available information:

```javascript
// Sanitised Google OSINT query builder
const OSINT_QUERIES = [
  `"${name}" site:linkedin.com`,            // LinkedIn verification
  `"${name}" "${company}" news`,            // Press coverage
  `"${name}" site:github.com`,             // Technical work
  `"${name}" site:trustpilot.com OR site:glassdoor.com`, // Reviews
  `"${name}" court OR lawsuit OR fraud`,   // Legal history
  `"${name}" "${position}" recommendation`, // Third-party validation
];
```

Results are passed directly into the AI analysis — no manual interpretation needed.

## Report Output

The HTML report is structured to be readable in under 3 minutes:

1. **Candidate header** — name, position applied for, screening date
2. **Consistency score** — 0–100 gauge with key discrepancy list
3. **Social media flags** — severity-coded (green/amber/red)
4. **Professional timeline** — CV vs. LinkedIn side-by-side
5. **Executive summary** — recommendation + top 3 concerns
6. **Raw data appendix** — all source data for verification

Every screening is logged to Airtable with the full structured output — building a searchable history for the hiring team.

## Results

<div class="result-box">
  <div class="result-label">Outcomes</div>
  <ul>
    <li>End-to-end screening: ~8 minutes vs. 2+ hours manually</li>
    <li>7 data sources queried per candidate — more than most human researchers cover</li>
    <li>Structured JSON output makes reports consistent and comparable across candidates</li>
    <li>Full screening log in Airtable — searchable history across all candidates</li>
    <li>Claude Haiku keeps per-candidate API cost under $0.03</li>
  </ul>
</div>

## Key Lessons

**Structure the AI output, don't parse prose.** Requiring `JSON.stringify`-able output from every Claude call meant zero parsing failures in production. Free-text summaries go into a `"summary"` string field — not the main data structure.

**Three focused calls beat one mega-prompt.** Splitting into consistency, social, and summary analyses gave cleaner outputs and made individual failure modes easier to debug than a single monolithic prompt.

**Always validate before writing.** Every report is checked for a minimum consistency score and at least one analysis block before being written to Airtable — preventing half-complete reports from appearing in the hiring log.
