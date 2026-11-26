---
layout: default
title: Production planner demo
permalink: /demo/production-planner/
description: A demo on synthetic data. Which seed varieties are short or long, how much to produce, where and by when. Built in Power BI, Power Apps, Power Automate and Excel, with Claude beside it.
---
{% comment %}
DRAFT 2026-11-15, rewritten 2026-11-26 for the Microsoft-only demo (Rasmus, 2026-11-24: Google and the custom
version archived; video and screenshots, no public link). Branch demo-page-2026-11-15. Not live. Copy needs Rasmus's
approval. Before it goes live: the Claude question run on the Semina model (demo/claude-questions.md in
seed-planning-demo) and the demo-track QC record. Fill the video link when it is recorded; empty hides the button.
{% endcomment %}
{% assign booking = "https://calendly.com/rasmuskampmann-info/30min" %}
{% assign video_microsoft = "" %}

<section class="offer-hero">
  <div class="container">
    <h1>Which varieties will you run out of?</h1>
    <p class="offer-sub">A seed company decides what to produce more than a season before it knows what it will sell, or what the fields will yield. This planner says per variety if you are short, balanced or long, and what to produce, where and by when.</p>
    <p class="offer-note">A demo on synthetic data. Semina Seeds is a fictional company: 30 varieties, 3 production sites in two hemispheres, 15 customers.</p>
  </div>
</section>

<section class="offer-section offer-section--alt">
  <div class="container">
    <h2>What it does</h2>
    <div class="offer-cards offer-cards--two">
      <article class="offer-card">
        <h3>Short, balanced or long.</h3>
        <p>Months of cover per variety, now and after the open production lands. Sellable stock only: lots on hold, failed or due for a germination retest are left out.</p>
      </article>
      <article class="offer-card">
        <h3>Forecasts corrected for bias.</h3>
        <p>Customers under-forecast. The planner measures what each customer bought against what they said, and puts the adjusted figure next to theirs. Every forecast is kept as a version.</p>
      </article>
      <article class="offer-card">
        <h3>How much, where, by when.</h3>
        <p>Net requirement, site, order-by date and hectares. Your most important varieties are planned on a bad-year yield. Switch between bad, normal and good years and every number moves by a rule you can read.</p>
      </article>
      <article class="offer-card">
        <h3>A second chance after a bad season.</h3>
        <p>When a yield estimate drops, an alert fires. If a site in the other hemisphere can still land seed before the need date, the planner proposes that order.</p>
      </article>
    </div>
    <p class="offer-note">Every number comes from plain rules in the database. No AI calculates anything. The rules are checked against a separate reference engine, field by field, on every build.</p>
  </div>
</section>

<section class="offer-section">
  <div class="container">
    <h2>Built in the Microsoft tools you already pay for</h2>
    <div class="offer-cards offer-cards--two">
      <article class="offer-card">
        <h3>Power BI</h3>
        <p>The board, the plan with its yield switch, the alerts and the lots. One model on Azure SQL, so every screen and every answer reads the same numbers.</p>
      </article>
      <article class="offer-card">
        <h3>Power Apps</h3>
        <p>Where a person acts: log a production stage or a yield estimate, and approve what Claude proposes. The app adds up nothing; the database does the sums.</p>
      </article>
      <article class="offer-card">
        <h3>Power Automate</h3>
        <p>The high alerts land in your inbox each morning, so nobody has to open a report to find out. A forecast typed in Excel is written back to the plan by a flow.</p>
      </article>
      <article class="offer-card">
        <h3>Excel</h3>
        <p>The forecast grid stays in Excel: what each customer said, what they usually buy, and the bias-adjusted figure next to it. Type your own number and submit.</p>
      </article>
    </div>
    {% if video_microsoft != "" %}<p><a href="{{ video_microsoft }}" target="_blank" rel="noopener">Watch the 4-minute walkthrough &rarr;</a></p>{% endif %}
  </div>
</section>

<section class="offer-section offer-section--alt">
  <div class="container">
    <h2>Claude on the side</h2>
    <p>Claude reads, explains and drafts. It never calculates a plan number and never changes data on its own. It files a proposal with the source attached, and a person approves it.</p>
    <p>Built in the demo:</p>
    <ul>
      <li>"How much should we produce, and by when?" asked in plain words and answered from the Power BI model, through Microsoft's own connector. Same number as the report.</li>
      <li>"Why are we producing this much?" answered from the plan, rule by rule.</li>
      <li>A grower's mail turned into a proposed stage update or yield estimate.</li>
    </ul>
    <p>Designed, not in the demo yet: lab report intake, forecast requests to customers, a weekly planning summary, unfilled demand captured from customer mails, field reports, customer meeting briefs and germination retest reminders.</p>
  </div>
</section>

<section class="offer-section offer-final">
  <div class="container offer-narrow">
    <h2>Plan production in Excel today?</h2>
    <p class="offer-lead">Book 20 minutes and I'll show you where your varieties would sit.</p>
    <div class="offer-ctas">
      <a href="{{ booking }}" class="offer-btn offer-btn--primary" target="_blank" rel="noopener">Book a call</a>
      <a href="{{ '/contact' | relative_url }}" class="offer-btn">Write me instead</a>
    </div>
  </div>
</section>
