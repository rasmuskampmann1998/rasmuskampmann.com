---
layout: default
title: Results
permalink: /results/
description: Results from the system Rasmus Kampmann built at Veginova, a seed company, and from his work at an accounting firm. A production plan with zero mismatches against the planner's spreadsheet, one revenue number tied to the official accounts, and a model at AUC 0.75.
---
{% assign booking = "https://calendly.com/rasmuskampmann-info/30min" %}

<section class="offer-hero">
  <div class="container">
    <h1>Results</h1>
    <p class="offer-sub">From the system I built at Veginova, the seed company where I work, and from my time at Digi-Tal Regnskab. The companies' own revenue, customers and prices stay private.</p>
  </div>
</section>

<section class="offer-section offer-section--alt">
  <div class="container">
    <div class="offer-cards">
      <article class="offer-card">
        <p class="offer-proof-num">0 mismatches</p>
        <h3>The production plan.</h3>
        <p>The plan lived in a spreadsheet and went stale every time a sale landed, and seed takes about a year to grow.</p>
        <p>Now it's a live plan built from sales, stock and incoming orders, with shortage warnings and what-if tests for higher sales, lower capacity and lost stock.</p>
        <p class="offer-cost">The production plan matches the planner's own spreadsheet with zero mismatches.</p>
        <p><a href="{{ '/projects/03-veginova-operations/' | relative_url }}">Read the case &rarr;</a></p>
      </article>
      <article class="offer-card">
        <p class="offer-proof-num">3 &rarr; 1</p>
        <h3>One revenue number.</h3>
        <p>The tax accounts and the invoices disagreed, so nobody trusted either.</p>
        <p>Now the invoices are the source, reconciled to the official 2024 accounts, and the remaining gap is explained by currency timing. Margin per variety is visible for the first time.</p>
        <p class="offer-cost">Three revenue numbers became one, tied to the official accounts.</p>
        <p><a href="{{ '/projects/04-veginova-invoices/' | relative_url }}">Read the case &rarr;</a></p>
      </article>
      <article class="offer-card">
        <p class="offer-proof-num">AUC 0.75</p>
        <h3>Who to call first.</h3>
        <p>At Digi-Tal Regnskab, an accounting firm, prospects already using one accounting product converted better, but there was no list of who used it.</p>
        <p>A model built on public registry data predicted it, and the list was reordered every morning before the first call.</p>
        <p class="offer-cost">Holdout AUC 0.75. The lift in conversions was never measured.</p>
        <p><a href="{{ '/projects/05-software-detection-ml/' | relative_url }}">Read the case &rarr;</a></p>
      </article>
    </div>
    <p class="offer-note"><a href="{{ '/portfolio/' | relative_url }}#projects">All projects</a></p>
  </div>
</section>

<section class="offer-section offer-final">
  <div class="container offer-narrow">
    <h2>Hire me by the hour.</h2>
    <p class="offer-lead">Freelance Power BI and Power Platform work, hybrid in Denmark or remote for Europe and the US. Book a 20-minute call, or write if you'd rather.</p>
    <div class="offer-ctas">
      <a href="{{ booking }}" class="offer-btn offer-btn--primary" target="_blank" rel="noopener">Book a call</a>
      <a href="{{ '/contact' | relative_url }}" class="offer-btn">Contact and CV</a>
    </div>
  </div>
</section>
