---
layout: default
title: Production planner demo
permalink: /demo/production-planner/
description: A demo on synthetic data. Which seed varieties are short or long, how much to produce, where and by when. The same numbers in Microsoft, Google or a custom app.
---
{% comment %}
DRAFT 2026-11-15, branch demo-page-2026-11-15. Not live. Copy needs Rasmus's approval.
Fill the links below when each version is live. An empty link hides its button.
{% endcomment %}
{% assign booking = "https://calendly.com/rasmuskampmann-info/30min" %}
{% assign video_custom = "" %}
{% assign video_google = "" %}
{% assign video_microsoft = "" %}
{% assign live_custom = "" %}
{% assign live_google = "" %}
{% assign copy_google = "" %}
{% assign live_microsoft = "" %}

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
    <p class="offer-note">Every number comes from plain rules in the database. No AI calculates anything. The same rules give the same result in all three versions, checked field by field on every build.</p>
  </div>
</section>

<section class="offer-section">
  <div class="container">
    <h2>Three versions, same numbers</h2>
    <div class="offer-cards offer-cards--two">
      <article class="offer-card">
        <h3>Microsoft</h3>
        <p>Azure SQL, Power BI, an Excel forecast grid and a Power App for production stages.</p>
        {% if video_microsoft != "" %}<p><a href="{{ video_microsoft }}" target="_blank" rel="noopener">Watch the 4-minute walkthrough &rarr;</a></p>{% endif %}
        {% if live_microsoft != "" %}<p><a href="{{ live_microsoft }}" target="_blank" rel="noopener">Open the report &rarr;</a></p>{% endif %}
      </article>
      <article class="offer-card">
        <h3>Google Workspace</h3>
        <p>One Google Sheet with Apps Script. No new licences. Your data stays in your own Drive.</p>
        {% if video_google != "" %}<p><a href="{{ video_google }}" target="_blank" rel="noopener">Watch the 4-minute walkthrough &rarr;</a></p>{% endif %}
        {% if live_google != "" %}<p><a href="{{ live_google }}" target="_blank" rel="noopener">Open the web app &rarr;</a></p>{% endif %}
        {% if copy_google != "" %}<p><a href="{{ copy_google }}" target="_blank" rel="noopener">Make your own copy &rarr;</a></p>{% endif %}
      </article>
      <article class="offer-card">
        <h3>Custom</h3>
        <p>A Postgres database with a web app. For teams on neither stack.</p>
        {% if video_custom != "" %}<p><a href="{{ video_custom }}" target="_blank" rel="noopener">Watch the 4-minute walkthrough &rarr;</a></p>{% endif %}
        {% if live_custom != "" %}<p><a href="{{ live_custom }}" target="_blank" rel="noopener">Open the app &rarr;</a></p>{% endif %}
      </article>
    </div>
  </div>
</section>

<section class="offer-section offer-section--alt">
  <div class="container">
    <h2>Claude on the side</h2>
    <p>Claude reads, explains and drafts. It never calculates a plan number and never changes data on its own. It files a proposal with the source attached, and a person approves it.</p>
    <p>Built in the demo:</p>
    <ul>
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
