---
layout: default
title: Contact
description: Hire Rasmus Kampmann, Freelance Power BI Consultant. Book a 20-minute call or email info@rasmuskampmann.com. Recruiters and companies use the same route.
---
{% assign booking = "https://calendly.com/rasmuskampmann-info/30min" %}
{% assign mail = site.author.email %}

<section class="offer-hero">
  <div class="container">
    <h1>Contact</h1>
    <p class="offer-sub">Recruiters and companies use the same route: book a 20-minute call or send an email. I reply within one working day.</p>
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
        <h3>Send an email.</h3>
        <p>Write to <a href="mailto:{{ mail }}">{{ mail }}</a> with the role or the project, the dates and the hours you have in mind.</p>
        <a href="mailto:{{ mail }}" class="offer-btn">Email me</a>
      </article>
    </div>
    <p class="offer-note" id="cv">For my CV, <a href="mailto:{{ mail }}?subject=CV%20request">email me</a> and I'll send the current version.</p>
    <p class="offer-note">Freelance by the hour, hours by agreement. Hybrid in Denmark up to three days a week, or remote for Europe and the US. Rate on request. I work in Danish, English and Spanish.</p>
    <p class="offer-note">Or find me on <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a>.</p>
  </div>
</section>
