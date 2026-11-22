---
layout: home
description: Rasmus Kampmann, Freelance Power BI Consultant in Odense, Denmark. Power BI Developer, Power Platform Consultant and Data Analyst. I build business systems that combine data, apps and AI for supply chain and agri-food companies. Hourly contracts, hybrid in Denmark or remote for Europe and the US.
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
    <p class="hero-background">Power BI Developer, Power Platform Consultant and Data Analyst. I build business systems that combine data, apps and AI for supply chain and agri-food companies. Hourly contracts on longer engagements, hybrid in Denmark up to three days a week or remote for Europe and the US. Rate on request.</p>
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
        <p>Semantic models and Power BI reports for sales, inventory and finance that load fast and show the number the database holds.</p>
        <p class="offer-tools"><strong>Tools:</strong> Power BI, DAX, Power Query</p>
        <p class="offer-case"><a href="{{ '/projects/veginova-power-bi/' | relative_url }}">Case: two semantic models and four reports &rarr;</a></p>
      </article>
      <article class="offer-card">
        <span class="offer-step">4</span>
        <h3>AI and automation</h3>
        <p>Claude beside the system, connected to the database through MCP, proposing changes a person approves.</p>
        <p class="offer-tools"><strong>Tools:</strong> Claude Code, VS Code, GitHub, MCP, Python</p>
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

    <div class="experience-timeline">

      <div class="experience-card">
        <p class="experience-date">Nov 2026 to now</p>
        <h4 class="experience-role">Freelance Power BI &amp; Power Platform Consultant</h4>
        <p class="experience-company">Own business · Odense, Denmark · hybrid or remote</p>
        <ul class="experience-bullets">
          <li>I take hourly contracts on longer engagements: Power BI, Power Platform, Azure SQL and Python.</li>
          <li>Hybrid in Denmark up to three days a week, or remote for Europe and the US.</li>
        </ul>
      </div>

      <div class="experience-card">
        <p class="experience-date">Aug 2023 to now</p>
        <h4 class="experience-role">Veginova Seeds</h4>
        <p class="experience-company">Family-owned seed company · Odense, Denmark · my employer</p>
        <p class="experience-transition">The supply chain and operations system the company runs on, from scattered Excel files to one Azure SQL database with apps, reports and AI on top. The first version ran on Postgres (Supabase); I tested Microsoft Fabric with a working prototype, then moved the system to Azure SQL in August 2026.</p>

        <div class="experience-subrole">
          <p class="experience-date">Jun 2026 to now</p>
          <p class="experience-subrole-title">Power BI &amp; Power Apps Developer</p>
          <ul class="experience-bullets">
            <li>Mapped sales, inventory, production and finance data from Excel, SharePoint and e-conomic into one source of truth.</li>
            <li>Power BI dashboards and semantic models for sales, inventory and finance.</li>
            <li>A Power Apps operations app for orders, invoices, stock, germination tests and month-end close.</li>
            <li>Data pipelines in Python and Azure Functions, refreshed every ten minutes during the working day.</li>
            <li>Lot traceability and quality control: a lot can only be sold once its germination test releases it.</li>
            <li>Claude set up to read seed packets and bills into rows a person confirms. Not yet in daily use.</li>
            <li><strong>Results:</strong> three revenue numbers became one, tied to the official accounts, and the production plan matches the planner's own spreadsheet with zero mismatches. Both are case studies on this site.</li>
          </ul>
          <p class="experience-stack"><strong>Stack:</strong> Azure SQL · T-SQL · Python · Azure Functions · Power BI · DAX · Power Apps · SharePoint · Excel · Claude Code</p>
        </div>

        <div class="experience-subrole">
          <p class="experience-date">May 2025 to Feb 2026</p>
          <p class="experience-subrole-title">Data Analyst</p>
          <p class="experience-transition">The first version of the operations and finance reporting, which became the foundation for the system that runs today.</p>
          <ul class="experience-bullets">
            <li>Power BI dashboards for operations and finance with DAX and Power Query.</li>
            <li>A Postgres database on Supabase and an operations and finance web app in Streamlit and Python.</li>
            <li>SQL on Excel files and e-conomic accounting exports, my first work with e-conomic data.</li>
            <li>An agriculture market intelligence platform that scraped news, regulations and market data from 228 sources with AI agents, and answered questions through retrieval-based chat.</li>
          </ul>
          <p class="experience-stack"><strong>Stack:</strong> Power BI · DAX · Power Query · SQL · Python · Postgres · Supabase · Streamlit · FastAPI · React · e-conomic</p>
        </div>

        <div class="experience-subrole">
          <p class="experience-date">Aug 2023 to May 2025</p>
          <p class="experience-subrole-title">Marketing &amp; Operations</p>
          <p class="experience-transition">Customer sourcing, trade fairs and visits to seed production partners in Costa Rica, Panama and Mexico. This is where I learned how seed is produced, tested, priced, sold and shipped, and that shapes every rule in the systems I build. The data work grew out of this role.</p>
        </div>
      </div>

      <div class="experience-card">
        <p class="experience-date">Feb to May 2026</p>
        <h4 class="experience-role">Digi-Tal Regnskab</h4>
        <p class="experience-company">Digital accounting firm for small businesses · Data Analyst (Commercial)</p>
        <p class="experience-transition">An outbound sales system from lead sourcing to CRM handoff, combining data, AI and automation, built in four months.</p>
        <ul class="experience-bullets">
          <li>Revenue and customer acquisition analysis across Meta, Google, LinkedIn, cold calling and inbound, reconciled to the accounts.</li>
          <li>Customer, churn and LinkedIn attribution analyses, so sales targeted customers who convert and stay.</li>
          <li>The ideal customer profile and lead scoring from Pipedrive CRM data and the Danish company registry (CVR).</li>
          <li>A machine learning model that predicts a prospect's accounting software, trained on 4,600+ rows, AUC 0.75 on holdout.</li>
          <li>Commission and forecast model: rebuilt the commission structure to weight MRR and LTV, removing the incentive to discount subscriptions to close.</li>
          <li>Lead sourcing, enrichment and CRM handoff automated with Python, Clay and the Claude API.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> Python · SQL · PostgreSQL · Pipedrive · Clay · HeyReach · Claude API · scikit-learn · XGBoost</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jan 2025 to Jan 2026</p>
        <h4 class="experience-role">Outlier</h4>
        <p class="experience-company">AI &amp; LLM Data Analyst · LLM evaluation in Danish</p>
        <p class="experience-transition">Reviewed and annotated 1,000+ Danish AI conversations used to train large language models. It taught me how LLMs answer, where they go wrong and how to evaluate their output, which I use when I build AI into business systems.</p>
        <p class="experience-stack"><strong>Skills:</strong> LLM evaluation · data annotation · prompt review · generative AI</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jun 2024 to Aug 2025</p>
        <h4 class="experience-role">Sira Logic</h4>
        <p class="experience-company">My first consultancy · AI &amp; Automation Consultant (independent)</p>
        <p class="experience-transition">Run alongside the seed company: AI and automation systems for B2B sales data, from data collection to scoring inside the CRM.</p>
        <ul class="experience-bullets">
          <li>Lead enrichment and scoring workflows with AI-assisted enrichment.</li>
          <li>CRM workflows automated in n8n and Make with HubSpot and GoHighLevel.</li>
          <li>Custom web scraping with Python and Apify.</li>
          <li>The whole cycle on my own: sales, scoping, build, deployment, handover. It closed in 2025 and taught me which automation is worth building.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> Python · SQL · n8n · Make · Clay · Apify · HubSpot · GoHighLevel · Claude API</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jan to Aug 2023</p>
        <h4 class="experience-role">Damstahl Danmark</h4>
        <p class="experience-company">Stainless steel distributor · Marketing &amp; Digital Graduate</p>
        <p class="experience-transition">Part-time alongside my BBA: product data in the ERP and CRM systems, and Excel dashboards for campaigns.</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Aug 2020 to Jun 2023</p>
        <h4 class="experience-role">Aarhus BSS, Aarhus University</h4>
        <p class="experience-company">Bachelor of Business Administration (BBA)</p>
        <p class="experience-transition">Exchange semester at Universidad del Pacífico, Peru, Aug to Dec 2022. Before that, Tietgen HHX with a marketing line, 2015 to 2018.</p>
      </div>

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
