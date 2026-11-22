---
layout: home
description: Freelance Power BI Consultant in Odense, Denmark. Power BI Developer, Power Platform Consultant and Data Analyst. I build business systems that combine data, apps and AI for supply chain and agri-food companies. Hourly contracts, hybrid in Denmark or remote for Europe and the US.
---
{% assign booking = "https://calendly.com/rasmuskampmann-info/30min" %}

<section class="offer-hero" id="top">
  <div class="container">
    <p class="offer-eyebrow">Rasmus Kampmann &middot; Odense, Denmark</p>
    <h1>Freelance Power BI Consultant</h1>
    <p class="offer-sub">Power BI Developer, Power Platform Consultant and Data Analyst. I build business systems that combine data, apps and AI for supply chain and agri-food companies.</p>
    <p class="offer-avail">Available for hourly freelance contracts, with hours by agreement. Hybrid in Denmark up to three days a week, or remote for Europe and the US.</p>
    <div class="offer-ctas">
      <a href="{{ booking }}" class="offer-btn offer-btn--primary" target="_blank" rel="noopener">Book a call</a>
      <a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" class="offer-btn" download>Download CV</a>
    </div>
    <div class="offer-badge">
      <img src="{{ '/assets/images/me/hero-portrait.jpg' | relative_url }}" alt="" width="44" height="44" />
      <p><strong>Power BI, Power Apps, Power Automate, Azure SQL, Python and Claude.</strong> Rate on request. The first call is 20 minutes, with me.</p>
    </div>
  </div>
</section>

<section class="offer-section offer-section--alt" id="what">
  <div class="container">
    <h2>One system in four layers, on the Microsoft data stack.</h2>
    <p class="offer-lead">At Veginova, the seed company where I work, I built all four layers myself. On a contract I take one layer or all four, inside your team or on my own.</p>
    <div class="offer-cards offer-cards--four">
      <article class="offer-card">
        <span class="offer-step">1</span>
        <h3>Data foundation</h3>
        <p>One source of truth with the business rules in the database, so sales, inventory and finance show the same number.</p>
        <p class="offer-tools"><strong>Tools:</strong> Azure SQL, T-SQL, Python, Azure Functions, Logic Apps</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-bi/' | relative_url }}">Case: three revenue numbers became one &rarr;</a></p>
      </article>
      <article class="offer-card">
        <span class="offer-step">2</span>
        <h3>Business applications</h3>
        <p>Apps where teams enter orders, stock and plans in one place instead of many spreadsheets. Excel stays as a front door.</p>
        <p class="offer-tools"><strong>Tools:</strong> Power Apps, Power Automate, Excel, SharePoint</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-platform-ai/' | relative_url }}">Case: a Power Apps operations app on Azure SQL &rarr;</a></p>
      </article>
      <article class="offer-card">
        <span class="offer-step">3</span>
        <h3>Reporting</h3>
        <p>Semantic models and Power BI dashboards for sales, inventory and finance. At Veginova the reports refresh themselves every ten minutes during the working day.</p>
        <p class="offer-tools"><strong>Tools:</strong> Power BI, DAX, Power Query</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-bi/' | relative_url }}">Case: two semantic models and four reports &rarr;</a></p>
      </article>
      <article class="offer-card">
        <span class="offer-step">4</span>
        <h3>AI and automation</h3>
        <p>Claude beside the system, connected to the database through MCP, proposing changes a person approves. I build with Claude Code in VS Code and GitHub.</p>
        <p class="offer-tools"><strong>Tools:</strong> Claude Code, VS Code, GitHub, MCP, Python</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-platform-ai/' | relative_url }}">Case: Claude Code, MCP and my sign-off on every release &rarr;</a></p>
      </article>
    </div>
    <p class="offer-note">I also build on Google Workspace and on custom stacks with Postgres and Python. <a href="{{ '/portfolio/' | relative_url }}#projects">Both case studies</a></p>
  </div>
</section>

<section class="offer-section" id="problems">
  <div class="container">
    <h2>Problems I solve</h2>
    <div class="offer-cards">
      <article class="offer-card">
        <h3>Three revenue numbers that disagree.</h3>
        <p>Three revenue numbers became one, tied to the official accounts, and revenue reconciles to the audited accounts on every change.</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-bi/' | relative_url }}">Power BI, SQL and data analytics &rarr;</a></p>
      </article>
      <article class="offer-card">
        <h3>A production plan that goes stale the day a sale lands.</h3>
        <p>The production plan matches the planner's own spreadsheet with zero mismatches, and it updates when sales or stock change.</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-bi/' | relative_url }}">Power BI, SQL and data analytics &rarr;</a></p>
      </article>
      <article class="offer-card">
        <h3>Stock numbers nobody trusts.</h3>
        <p>Stock is calculated from every movement since the last count, lot by lot, and a lot can only be sold once its quality test releases it.</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-platform-ai/' | relative_url }}">Power Platform and AI development &rarr;</a></p>
      </article>
    </div>
  </div>
</section>

<section class="offer-section offer-section--alt" id="hire">
  <div class="container offer-narrow">
    <h2>How to hire me</h2>
    <ul class="offer-list">
      <li>I work by the hour on longer engagements, and the rate is on request.</li>
      <li>I can work inside your team next to your own people, or as the one person who builds the system end to end.</li>
      <li>Hybrid in Denmark up to three days a week, or remote for clients in Europe and the US. Hours by agreement.</li>
      <li>I work in Danish, English and Spanish.</li>
      <li>The first step is a 20-minute call. Book it on the calendar, or write to <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>.</li>
    </ul>
    <div class="offer-ctas">
      <a href="{{ booking }}" class="offer-btn offer-btn--primary" target="_blank" rel="noopener">Book a call</a>
      <a href="mailto:{{ site.author.email }}" class="offer-btn">Email me</a>
    </div>
  </div>
</section>

<section class="offer-section" id="experience">
  <div class="container offer-narrow">
    <h2>Experience</h2>
    <ol class="offer-timeline">
      <li>
        <span class="offer-timeline-when">Nov 2026 to now</span>
        <strong>Freelance Power BI &amp; Power Platform Consultant.</strong> I take hourly contracts on longer engagements: Power BI, Power Platform, Azure SQL and Python. Hybrid in Denmark up to three days a week, or remote for Europe and the US.
      </li>
      <li>
        <span class="offer-timeline-when">Aug 2023 to now</span>
        <strong>Veginova Seeds, Odense.</strong> A family-owned seed company and my employer. I build and run its system: Excel on SharePoint and the accounting export feed an Azure SQL database with the business rules, with Power BI reports and a Power Apps operations app on top.
        <p class="offer-role"><span>Jun 2026 to now</span> Power BI &amp; Power Apps Developer</p>
        <p class="offer-role"><span>May 2025 to Feb 2026</span> Data Analyst</p>
        <p class="offer-role"><span>Aug 2023 to May 2025</span> Marketing &amp; Operations, with production visits in Costa Rica, Panama and Mexico</p>
      </li>
      <li>
        <span class="offer-timeline-when">Feb 2026 to May 2026</span>
        <strong>Digi-Tal Regnskab, Data Analyst (Commercial).</strong> I built the commercial data infrastructure of an accounting firm in four months, and a model that predicts a prospect's accounting software at AUC 0.75 on holdout.
      </li>
      <li>
        <span class="offer-timeline-when">Jan 2025 to Jan 2026</span>
        <strong>Outlier, AI &amp; LLM Data Analyst.</strong> LLM evaluation in Danish.
      </li>
      <li>
        <span class="offer-timeline-when">Jun 2024 to Aug 2025</span>
        <strong>Sira Logic, AI &amp; Automation Consultant (independent).</strong> My first consultancy: AI and automation for B2B sales data, from scraping and enrichment to scoring and CRM automation, in Python, SQL, n8n, Clay and Apify.
      </li>
      <li>
        <span class="offer-timeline-when">Jan 2023 to Aug 2023</span>
        <strong>Damstahl Danmark, Marketing &amp; Digital Graduate.</strong> Product data in ERP and CRM.
      </li>
      <li>
        <span class="offer-timeline-when">Aug 2020 to Jun 2023</span>
        <strong>Aarhus BSS, Aarhus University, BBA.</strong> Bachelor of Business Administration, with an exchange semester at Universidad del Pacífico in Peru in 2022.
      </li>
    </ol>
    <p class="offer-note">Certificates: Google Data Analytics, Artificial Intelligence: Implications for Business Strategy, Power BI Fundamentals.</p>
    <p class="offer-note">More detail on the <a href="{{ '/portfolio/' | relative_url }}#experience">portfolio page</a> and on <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a>.</p>
  </div>
</section>

<section class="offer-section offer-final" id="contact">
  <div class="container offer-narrow">
    <h2>Hire me by the hour.</h2>
    <p class="offer-lead">Book a 20-minute call, or write to {{ site.author.email }}. I reply within one working day.</p>
    <div class="offer-ctas">
      <a href="{{ booking }}" class="offer-btn offer-btn--primary" target="_blank" rel="noopener">Book a call</a>
      <a href="{{ '/contact' | relative_url }}" class="offer-btn">Contact and CV</a>
    </div>
  </div>
</section>
