---
layout: default
title: Get in touch
description: Book a call or write. Operations systems for seed and agriculture companies. I reply within one working day.
---
{% assign booking = "https://calendly.com/rasmuskampmann-info/30min" %}
{% assign mail = site.author.email %}

<section class="offer-hero">
  <div class="container">
    <h1>Get in touch.</h1>
    <p class="offer-sub">Tell me how you plan production and track stock today. I'll tell you honestly whether I can help.</p>
  </div>
</section>

<section class="offer-section offer-section--alt">
  <div class="container">
    <div class="offer-cards offer-cards--two offer-routes">
      <article class="offer-card">
        <h3>Book a call.</h3>
        <p>30 minutes on the calendar, about 20 of talking. The call is with me.</p>
        <a href="{{ booking }}" class="offer-btn offer-btn--primary" target="_blank" rel="noopener">Book a call</a>
      </article>
      <article class="offer-card">
        <h3>Write instead.</h3>
        <p>Pick what it's about. I reply within one working day.</p>
        <ul class="offer-topics">
          <li><a href="mailto:{{ mail }}?subject=Production%20Planner">Production Planner &rarr;</a></li>
          <li><a href="mailto:{{ mail }}?subject=Stock%20and%20lot%20control">Stock &amp; lot control &rarr;</a></li>
          <li><a href="mailto:{{ mail }}?subject=Operations%20system">Operations system &rarr;</a></li>
          <li><a href="mailto:{{ mail }}?subject=Not%20sure%20yet">Not sure yet &rarr;</a></li>
        </ul>
      </article>
    </div>
    <p class="offer-note">Or find me on <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a>. I work in English and Spanish.</p>
  </div>
</section>
