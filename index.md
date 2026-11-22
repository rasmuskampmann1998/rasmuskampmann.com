---
layout: home
description: Rasmus Kampmann, Freelance Power BI Consultant in Odense, Denmark. Power BI, Power Apps, Azure SQL and Python. Hourly contracts on longer engagements, hybrid in Denmark or remote for Europe and the US.
redirect_from:
  - /projects/01-cold-call-funnel/
  - /projects/02-channel-performance/
  - /projects/05-software-detection-ml/
---
{% assign booking = "https://calendly.com/rasmuskampmann-info/30min" %}

<section class="hero-centered" id="top">
  <div class="container">
    <div class="hero-avatar">
      <img src="{{ '/assets/images/me/hero-portrait.jpg?v=3' | relative_url }}" alt="Rasmus Kampmann" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
    </div>
    <p class="hero-name">Hi, I'm Rasmus Kampmann</p>
    <h1>Freelance Power BI Consultant</h1>
    <ul class="hero-stack">
      <li>Power BI</li>
      <li>Power Apps</li>
      <li>Azure SQL</li>
      <li>Python</li>
    </ul>
    <p class="hero-background">I build the data foundation, the apps and the Power BI reports a business runs on, on the Microsoft data stack. Hourly contracts on longer engagements, hybrid in Denmark up to three days a week or remote for Europe and the US. Rate on request.</p>
    <div class="hero-social">
      <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener" aria-label="LinkedIn">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
      </a>
      <a href="mailto:{{ site.author.email }}" aria-label="Email">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 12.713l-11.985-9.713h23.97l-11.985 9.713zm0 2.574l-12-9.725v15.438h24v-15.438l-12 9.725z"/></svg>
      </a>
    </div>
    <div class="hero-ctas-centered">
      <a href="{{ booking }}" class="btn-pill btn-pill--primary" target="_blank" rel="noopener">Book a call</a>
      <a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" class="btn-pill btn-pill--ghost" download>Download CV</a>
    </div>
  </div>
</section>

<section class="offer-section offer-section--alt" id="what">
  <div class="container">
    <span class="eyebrow">What I do</span>
    <h2>One system in four layers, on the Microsoft data stack.</h2>
    <p class="offer-lead">On a contract I take one layer or all four, inside your team or as the one person who builds it end to end.</p>
    <div class="offer-cards offer-cards--four">
      <article class="offer-card">
        <span class="offer-step">1</span>
        <h3>Data foundation</h3>
        <p>One source of truth with the business rules in the database, so sales, inventory and finance show the same number.</p>
        <p class="offer-tools"><strong>Tools:</strong> Azure SQL, T-SQL, Python, Azure Functions</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-bi/' | relative_url }}">Case: three revenue numbers became one &rarr;</a></p>
      </article>
      <article class="offer-card">
        <span class="offer-step">2</span>
        <h3>Business apps</h3>
        <p>Apps where teams enter orders, stock and plans in one place instead of many spreadsheets. Excel stays as a front door.</p>
        <p class="offer-tools"><strong>Tools:</strong> Power Apps, Power Automate, SharePoint</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-platform-ai/' | relative_url }}">Case: a Power Apps operations app on Azure SQL &rarr;</a></p>
      </article>
      <article class="offer-card">
        <span class="offer-step">3</span>
        <h3>Reporting</h3>
        <p>Semantic models and Power BI reports for sales, inventory and finance that load fast and show the number the database holds.</p>
        <p class="offer-tools"><strong>Tools:</strong> Power BI, DAX, Power Query</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-bi/' | relative_url }}">Case: two semantic models and four reports &rarr;</a></p>
      </article>
      <article class="offer-card">
        <span class="offer-step">4</span>
        <h3>AI and automation</h3>
        <p>Claude beside the system, connected to the database through MCP, proposing changes a person approves.</p>
        <p class="offer-tools"><strong>Tools:</strong> Claude Code, MCP, Python, GitHub</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-platform-ai/' | relative_url }}">Case: Claude Code, MCP and my sign-off on every release &rarr;</a></p>
      </article>
    </div>
    <p class="offer-note">I also build on Google Workspace and on custom stacks with Postgres and Python.</p>
  </div>
</section>

<section class="projects is-large" id="projects">
  <div class="container">
    <span class="eyebrow">Work</span>
    <h2>Case studies</h2>
    <p class="section-sub">Two case studies from the system I built at Veginova, my family's seed company, where I work. Its revenue, customers and prices stay private.</p>
    {% assign sorted_projects = site.projects | where_exp: "p", "p.archived != true" | sort: "order" %}
    <div class="projects-grid-large">
      {% for project in sorted_projects %}{% include project-card.html project=project %}{% endfor %}
    </div>
    <div class="offer-cards">
      <article class="offer-card">
        <p class="offer-proof-num">0 mismatches</p>
        <h3>The production plan</h3>
        <p>A live plan from sales, stock and incoming. It matches the planner's own spreadsheet with zero mismatches.</p>
      </article>
      <article class="offer-card">
        <p class="offer-proof-num">3 &rarr; 1</p>
        <h3>One revenue number</h3>
        <p>Three revenue numbers became one, reconciled to the audited accounts on every change.</p>
      </article>
      <article class="offer-card">
        <p class="offer-proof-num">Lot by lot</p>
        <h3>Stock and quality</h3>
        <p>Stock is calculated from every movement since the last count, and a lot can only be sold once its quality test releases it.</p>
      </article>
    </div>
  </div>
</section>

<section class="experience-section" id="experience">
  <div class="container">
    <span class="eyebrow">Background</span>
    <h2>Experience</h2>
    <div class="offer-faq">

      <details open>
        <summary>Nov 2026 to now &middot; Freelance Power BI &amp; Power Platform Consultant</summary>
        <p>My own business in Odense. Hourly contracts on longer engagements: Power BI, Power Platform, Azure SQL and Python.</p>
      </details>

      <details open>
        <summary>Aug 2023 to now &middot; Veginova Seeds, my employer</summary>
        <p>A family-owned seed company in Odense. Excel on SharePoint and the accounting export feed an Azure SQL database with the business rules, with Power BI reports and a Power Apps operations app on top. The first version ran on Postgres (Supabase); I tested Microsoft Fabric with a prototype, then moved the system to Azure SQL in August 2026.</p>
        <p><strong>Jun 2026 to now:</strong> Power BI &amp; Power Apps Developer. <strong>May 2025 to Feb 2026:</strong> Data Analyst. <strong>Aug 2023 to May 2025:</strong> Marketing &amp; Operations, with trade fairs, customers and production visits in Costa Rica, Panama and Mexico.</p>
        <p class="experience-stack"><strong>Stack:</strong> Azure SQL, T-SQL, Power BI, DAX, Power Apps, Power Automate, Python, Claude Code</p>
      </details>

      <details>
        <summary>Feb to May 2026 &middot; Digi-Tal Regnskab, Data Analyst (Commercial)</summary>
        <p>CRM, ad and registry data for an accounting firm, brought into one source of truth in four months.</p>
        <ul>
          <li>Commission and forecast model, rebuilt to weight MRR and LTV.</li>
          <li>Revenue channel analysis: close rate, conversion and time to close, reconciled to the accounts.</li>
          <li>A model that predicts a prospect's accounting software from public registry data, at AUC 0.75 on holdout.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> SQL, Python, PostgreSQL, n8n, Excel, Pipedrive, Clay</p>
      </details>

      <details>
        <summary>Jan 2025 to Jan 2026 &middot; Outlier, AI &amp; LLM Data Analyst</summary>
        <p>LLM evaluation in Danish.</p>
      </details>

      <details>
        <summary>Jun 2024 to Aug 2025 &middot; Sira Logic, AI &amp; Automation Consultant</summary>
        <p>My first consultancy: AI and automation for B2B sales data, from scraping and enrichment to scoring and CRM automation. Sales, scoping, build, deployment and handover on my own.</p>
        <p class="experience-stack"><strong>Stack:</strong> SQL, Python, n8n, Clay, Apify, HubSpot</p>
      </details>

      <details>
        <summary>Jan to Aug 2023 &middot; Damstahl Danmark, Marketing &amp; Digital Graduate</summary>
        <p>Product data in ERP and CRM.</p>
      </details>

      <details>
        <summary>Aug 2020 to Jun 2023 &middot; Aarhus BSS, Aarhus University, BBA</summary>
        <p>Bachelor of Business Administration, with an exchange semester at Universidad del Pac&iacute;fico in Peru in 2022.</p>
      </details>

    </div>
  </div>
</section>

<section class="about-two-col" id="about">
  <div class="container">
    <div class="about-two-col-grid">
      <div class="about-two-col-text">
        <span class="eyebrow">About</span>
        <h2>About me</h2>
        <p>I started in marketing and operations at <strong>Veginova</strong>, a family-owned seed company in Odense, sourcing customers, running trade fairs and visiting production in Costa Rica, Panama and Mexico. The data work grew out of that job.</p>
        <p>So when a report says a variety is running short, I know which process produced that number and where it breaks.</p>
        <div class="offer-faq">
          <details>
            <summary>What the system at Veginova covers</summary>
            <ul>
              <li>Excel stays the front door, with an Azure SQL database and its business rules behind it. It refreshes every ten minutes during the working day.</li>
              <li>Inventory and lot traceability: stock is calculated from every movement since the last count, lot by lot.</li>
              <li>Quality control: a lot can only be sold once its quality test releases it.</li>
              <li>Production planning from safety stock, expected sales, stock and incoming, matching the planner's spreadsheet with zero mismatches.</li>
              <li>Revenue reconciles to the audited accounts on every change.</li>
            </ul>
          </details>
          <details>
            <summary>How I use AI</summary>
            <p>I build with Claude Code in VS Code and GitHub, connect Claude to the database through MCP, and automate with Power Automate and Python. AI drafts from written procedures, and I review and sign off every release.</p>
            <p>In the systems I build, the numbers come from the database and a person confirms what the AI proposes.</p>
          </details>
          <details>
            <summary>The technical layer</summary>
            <p>Power BI end to end: semantic models, DAX, Power Query, report design, distribution and access. I connect it to the sources a business already runs on: Azure SQL, SQL Server, PostgreSQL, SharePoint, Excel and APIs.</p>
            <p>Beyond reports: data modelling in SQL, apps in Power Apps, automation with Power Automate and Python. I also build on Google Workspace and on custom stacks with Postgres and Python.</p>
          </details>
          <details>
            <summary>Certificates and languages</summary>
            <p>Google Data Analytics, Artificial Intelligence: Implications for Business Strategy (MIT Sloan), Power BI Fundamentals (DataCamp). I work in Danish, English and Spanish.</p>
          </details>
        </div>
      </div>
      <div class="about-two-col-photo">
        <img src="{{ '/assets/images/me/photo-2.jpg' | relative_url }}" alt="Rasmus Kampmann" loading="lazy" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
      </div>
    </div>
  </div>
</section>

<section class="offer-section offer-section--alt" id="hire">
  <div class="container offer-narrow">
    <span class="eyebrow">Contracts</span>
    <h2>How I work</h2>
    <ul class="offer-list">
      <li>By the hour on longer engagements. Rate on request, hours by agreement.</li>
      <li>Inside your team next to your own people, or as the one person who builds the system end to end.</li>
      <li>Hybrid in Denmark up to three days a week, or remote for Europe and the US.</li>
      <li>You explain your business once: I hold the whole picture from the database to the report.</li>
      <li>I document what I build, so your own people can run and change it after the contract ends.</li>
    </ul>
  </div>
</section>

<section class="cta-soft" id="contact">
  <div class="container">
    <span class="eyebrow">Contact</span>
    <h2>Hire me by the hour.</h2>
    <p class="section-sub">Book a 20-minute call, or write to <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> with the project, the dates and the hours. Recruiters and companies use the same route, and I reply within one working day.</p>
    <a href="{{ booking }}" class="btn-primary" target="_blank" rel="noopener">Book a call &rarr;</a>
    <p class="cta-soft-footnote" id="cv"><a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" download>Download my CV (PDF)</a> &middot; <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a></p>
  </div>
</section>
