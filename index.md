---
layout: home
title: Home
description: I take the numbers your business already has and put them on one screen you can trust. Power BI, SQL, automation. Odense, Denmark.
---

<section class="hero-centered">
  <div class="container">
    <div class="hero-avatar">
      <img src="{{ '/assets/images/me/hero-portrait.jpg?v=3' | relative_url }}" alt="Rasmus Kampmann" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
    </div>
    <p class="hero-name">Hi, I'm Rasmus Kampmann</p>
    <h1>Power BI Developer &amp; Data Analyst</h1>
    <ul class="hero-stack">
      <li>Power BI</li>
      <li>SQL</li>
      <li>Microsoft Fabric</li>
      <li>Python</li>
    </ul>
    <p class="hero-slogan">From Excel chaos to <span class="highlight">Power BI clarity.</span></p>
    <p class="hero-background">Your numbers live in files that do not agree. Excel says one thing, the system says another, and someone rebuilds the report by hand every week. I connect it all into one dashboard that updates itself.</p>
    <div class="hero-social">
      <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener" aria-label="LinkedIn">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
      </a>
      <a href="{{ site.author.github }}" target="_blank" rel="noopener" aria-label="GitHub">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.4 3-.405 1.02.005 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
      </a>
      <a href="mailto:{{ site.author.email }}" aria-label="Email">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 12.713l-11.985-9.713h23.97l-11.985 9.713zm0 2.574l-12-9.725v15.438h24v-15.438l-12 9.725z"/></svg>
      </a>
    </div>
    <div class="hero-ctas-centered">
      <a href="#projects" class="btn-pill btn-pill--ghost">View Projects</a>
      <a href="{{ '/contact' | relative_url }}" class="btn-pill btn-pill--primary">Get in touch</a>
    </div>
    <p class="hero-cv-link">
      <a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" download>↓ CV (EN)</a>
      <span style="margin: 0 10px; color: var(--text-muted);">·</span>
      <a href="{{ '/assets/files/rasmus-kampmann-cv-da.pdf' | relative_url }}" download>↓ CV (DA)</a>
    </p>
  </div>
</section>

<section class="skills-grid-section" id="skills">
  <div class="container">
    <span class="eyebrow">Skills</span>
    <h2>What I Do</h2>
    <p class="section-sub">I do one thing. I take the numbers your business already has and put them on one screen you can trust. Five tools do the work.</p>
    <div class="skills-grid">

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="13" width="4" height="7" rx="0.5"/>
            <rect x="10" y="7" width="4" height="13" rx="0.5"/>
            <rect x="17" y="3" width="4" height="17" rx="0.5"/>
          </svg>
        </div>
        <h3>Power BI</h3>
        <p>The screen you look at. Charts and numbers built around your decisions: what sold, what it cost, what is left. Semantic models, DAX, and report design underneath, so it stays fast and correct.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <ellipse cx="12" cy="5" rx="9" ry="3"/>
            <path d="M3 5v6c0 1.66 4 3 9 3s9-1.34 9-3V5"/>
            <path d="M3 11v6c0 1.66 4 3 9 3s9-1.34 9-3v-6"/>
          </svg>
        </div>
        <h3>SQL</h3>
        <p>The order underneath. One place where every number lives, so every report shows the same figure. I connect it to what you already use: SQL Server, PostgreSQL, SharePoint, Excel, APIs.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="4" width="18" height="16" rx="1.5"/>
            <line x1="3" y1="9" x2="21" y2="9"/>
            <line x1="3" y1="14" x2="21" y2="14"/>
            <line x1="9" y1="4" x2="9" y2="20"/>
            <line x1="15" y1="4" x2="15" y2="20"/>
          </svg>
        </div>
        <h3>Excel</h3>
        <p>Where your data starts, and that is fine. I keep Excel as the input and make it safe: locked tables, clear templates, no formulas that break when someone sorts a column.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.5 10a8.5 8.5 0 0 0-14.6-4.3L3 8.5"/>
            <polyline points="3 3.5 3 8.5 8 8.5"/>
            <path d="M3.5 14a8.5 8.5 0 0 0 14.6 4.3L21 15.5"/>
            <polyline points="21 20.5 21 15.5 16 15.5"/>
          </svg>
        </div>
        <h3>Automation</h3>
        <p>The end of copy-paste. Files flow in on their own and reports update themselves. Power Query, Power Automate, and n8n do the moving. Nobody retypes anything.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="16 18 22 12 16 6"/>
            <polyline points="8 6 2 12 8 18"/>
            <line x1="14" y1="4" x2="10" y2="20"/>
          </svg>
        </div>
        <h3>Python</h3>
        <p>The heavy lifting. Forecasts, big cleanups, and checks that spreadsheets cannot do, running on a schedule instead of by hand.</p>
      </div>

    </div>
  </div>
</section>

<section class="projects is-large" id="projects">
  <div class="container">
    <span class="eyebrow">Explore my work</span>
    <h2>My Projects</h2>
    <p class="section-sub">Three builds, one story: messy files in, one trusted screen out. Built with synthetic data where a client is involved. Written so you do not need to be a data person to follow them.</p>
    {% assign sorted_projects = site.projects | where_exp: "p", "p.archived != true" | sort: "order" %}
    <div class="projects-grid-large">
      {% for project in sorted_projects %}{% include project-card.html project=project %}{% endfor %}
    </div>
  </div>
</section>

<section class="about-two-col" id="about-strip">
  <div class="container">
    <div class="about-two-col-grid">
      <div class="about-two-col-text">
        <span class="eyebrow">Learn more</span>
        <h2>About Me</h2>
        <p>Hi, I'm Rasmus. I take the numbers your business already has and put them on one screen you can trust.</p>
        <p>I didn't start in data. I started in marketing and operations at <strong>Veginova</strong>, my family's seed company in Odense: sourcing customers, running trade fairs, and visiting production in Costa Rica, Panama, and Mexico. I learned what the numbers meant by collecting them, years before I built a dashboard on them.</p>
        <p>That's what makes the reporting different. When a report says a variety is running short or a customer isn't profitable, I know which process produced that number and where it breaks, because I worked in the process. The role grew into the data work, and I moved into it from there.</p>
        <p style="margin-top: 28px;"><strong>Does this sound like your Monday?</strong></p>
        <ul>
          <li>Your numbers live in five places and they do not agree.</li>
          <li>The same report gets rebuilt by hand every week. Usually by you.</li>
          <li>Excel says one thing. The system says another. Nobody knows which is right.</li>
          <li>You sell every day but do not know what you actually earn per product, per customer, per channel.</li>
          <li>One wrong formula and the pricing is off. It has happened before.</li>
          <li>You want AI, but the data under it is a mess.</li>
        </ul>
        <p>If two of these are true, that is the problem I fix.</p>
        <p style="margin-top: 28px;"><strong>What runs today</strong></p>
        <ul>
          <li>A system that reads supplier invoices line by line, a person approves what it found, and the accounts stay clean. Live at Veginova.</li>
          <li>A seasonal sales forecast that feeds the production plan.</li>
          <li>A profitability dashboard checked against the accounts, line by line.</li>
          <li>A prediction model at a fintech firm, right about three times out of four, running in production.</li>
        </ul>
        <p id="two-layers-of-ai" style="margin-top: 28px;"><strong>Two layers of AI</strong></p>
        <p>AI in my work comes in two layers.</p>
        <p>The AI I implement for the business: LLM extraction with human approval, Copilot on the semantic model, and predictive modelling as classical ML: forecasting, scoring, classification.</p>
        <p>The AI I build with: an agentic setup where Claude Code operates in GitHub, pulls context from Supabase, runs my library of reusable skills, and connects to my tools through MCP. One person, the delivery speed of a small team.</p>
        <p>Between the two layers, the source of truth stays deterministic. Trust is engineering, not generation.</p>
        <p style="margin-top: 28px;"><strong>The technical layer</strong></p>
        <p>Today I own BI and reporting across sales, operations, and production at Veginova. The data landscape is moving onto Azure SQL Database, and that migration is under way now. I evaluated Microsoft Fabric end to end with a working prototype before landing on Azure.</p>
        <p>I specialise in Power BI end to end: semantic models, DAX, Power Query, report design, distribution, and access management. I connect Power BI to the sources the business already runs on: SQL Server, PostgreSQL, Azure SQL, SharePoint, Excel, APIs, and third-party platforms.</p>
        <p>Beyond dashboards: data modelling in SQL, workflow automation with Power Automate and Python, and forecasting in Python notebooks.</p>
        <p style="margin-top: 28px;">Most of my experience is from small companies and my own. Close to the decisions, owning the work end to end.</p>
        <p><strong>Certifications:</strong> Google Data Analytics · Artificial Intelligence: Implications for Business Strategy (MIT Sloan) · Power BI Fundamentals (DataCamp) · Microsoft PL-300: Power BI Data Analyst (in preparation).</p>
        <p>Danish, English, Spanish, with clients and partners across Europe and Latin America.</p>
        <p style="margin-top: 28px;"><strong>Working with me</strong></p>
        <p>One person, full responsibility. I scope the project, build it, document it, and hand it over. Nothing falls between chairs, because there are no chairs.</p>
        <p>I hold the whole picture from end to end. You explain your business once. I take it from there: your files, the data model, the dashboard, the training.</p>
        <p>No cure, no pay. Before I start, we agree in writing exactly what the dashboard must do. If it does not do that, you do not pay.</p>
        <p>Fixed price, clear end date. And when I leave, you own everything: documentation, training, no dependency on me.</p>
        <p><em>Based in Odense, Denmark. Open to on-site roles.</em></p>
      </div>
      <div class="about-two-col-photo">
        <img src="{{ '/assets/images/me/photo-2.jpg' | relative_url }}" alt="Rasmus Kampmann" loading="lazy" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
      </div>
    </div>
  </div>
</section>

<section class="experience-section" id="experience">
  <div class="container">
    <span class="eyebrow">3+ years of experience</span>
    <h2>Experience</h2>
    <p class="section-sub">Roles where I built the data systems, dashboards, and automation behind real commercial decisions.</p>

    <div class="experience-timeline">

      <div class="experience-card">
        <p class="experience-date">Aug 2023 to now</p>
        <h4 class="experience-role">Veginova Seeds</h4>
        <p class="experience-company">Family-owned seed company · Odense, Denmark</p>
        <p class="experience-transition">International growers, distributors, and production partners across Europe and Latin America. (Spring 2026: role at Digi-Tal Regnskab, see below.)</p>

        <div class="experience-subrole">
          <p class="experience-date">Jun 2026 to now</p>
          <h5 class="experience-subrole-title">Power BI Developer</h5>
          <p class="experience-transition">Back at Veginova with responsibility for BI and reporting across sales, operations, and production. Driving the consolidation of the entire data landscape into one unified Microsoft ecosystem.</p>
          <ul class="experience-bullets">
            <li>Architecture: Azure SQL Database as the operational data layer, Power BI as the decision layer. Migration in progress. I evaluated Microsoft Fabric end to end with a working prototype before landing on Azure.</li>
            <li>Automated line-level invoice extraction with the Claude API: confidence scores and human approval via Power BI translytical task flows. Power Automate for event-driven file synchronisation. Excel inputs as locked tables on SharePoint.</li>
            <li>Sales and contribution margin dashboards, a seasonal sales forecast, and one unified source of truth reconciled to the accounts. Published as case studies on this site.</li>
          </ul>
          <p class="experience-stack"><strong>Stack:</strong> Azure SQL · Power BI · DAX · T-SQL · Python · Power Automate · Claude Code</p>
        </div>

        <div class="experience-subrole">
          <p class="experience-date">May 2025 to Feb 2026</p>
          <h5 class="experience-subrole-title">Data Analyst</h5>
          <p class="experience-transition">Promoted to ownership of reporting and data infrastructure across sales, operations, and production, and the analyses management steered by.</p>
          <ul class="experience-bullets">
            <li>Owned the shared data foundation: Power BI dashboards, SQL data models, and automated data flows as one source of truth for sales, operations, and production.</li>
            <li>Standardised metric definitions across sales, operations, and production so dashboard numbers matched the systems.</li>
            <li>Automated recurring reporting workflows so reports stopped being rebuilt by hand each week.</li>
          </ul>
          <p class="experience-stack"><strong>Stack:</strong> SQL · Power BI · DAX · Python · Excel · Supabase · Claude Code</p>
        </div>

        <div class="experience-subrole">
          <p class="experience-date">Aug 2023 to May 2025</p>
          <h5 class="experience-subrole-title">Marketing &amp; Operations</h5>
          <p class="experience-transition">Broad commercial role in the family business. The foundation for everything I do with data today.</p>
          <ul class="experience-bullets">
            <li>B2B marketing and lead sourcing (Clay) toward international wholesale, distributor, and grower customers. Trade fairs and customer events in Denmark.</li>
            <li>Production visits in Costa Rica, Panama, and Mexico. In Costa Rica also company establishment and dialogue with local partners.</li>
            <li>Connected ERP, CRM, and operational tools into reliable data flows. The role grew into the data work: the transition to data analyst came from there.</li>
          </ul>
          <p class="experience-stack"><strong>Stack:</strong> Microsoft Office · Clay · n8n · Supabase · Apify · API sources · GitHub</p>
        </div>
      </div>

      <div class="experience-card">
        <p class="experience-date">Feb to May 2026</p>
        <h4 class="experience-role">Data Analyst (Commercial)</h4>
        <p class="experience-company">Digi-Tal Regnskab</p>
        <p class="experience-transition">Built the commercial data infrastructure in four months: CRM, ad, and registry data unified into one source of truth, and the models and analyses on top. Recruited on the back of my Sira Logic data work.</p>
        <ul class="experience-bullets">
          <li>Commission and forecast model: rebuilt the commission structure to weight MRR and LTV, removing the incentive to discount subscriptions to close.</li>
          <li>Revenue channel analysis: close rate, conversion, and how long deals took to close across paid, cold outreach, and inbound, with revenue figures reconciled to the accounts.</li>
          <li>Predictive models: ICP and lead scoring with strong holdout performance, plus an ML model predicting prospects' accounting software from public registry data (holdout AUC 0.75).</li>
          <li>Churn and segmentation analysis: customer and prospect base segmented into active, lead, lost, and inactive cohorts. Surfaced funnel drop-off and the patterns behind closed deals.</li>
        </ul>
        <p class="experience-transition">Resigned when the family relocated back to Denmark. The role was fully remote, and I wanted to be back on-site, close to the business.</p>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Python · PostgreSQL · n8n · Excel · Pipedrive · Clay · Claude Code</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jun 2024 to Aug 2025</p>
        <h4 class="experience-role">Data &amp; AI Consultant (Independent)</h4>
        <p class="experience-company">Sira Logic</p>
        <p class="experience-transition">Own consulting business: end-to-end data and automation systems for B2B companies, from data collection to operationalised scoring in the clients' CRM.</p>
        <ul class="experience-bullets">
          <li>Scraping, AI-assisted enrichment and qualification, scoring, CRM automation, and lead systems combined in one flow. Qualification accuracy up by roughly a third.</li>
          <li>Custom web scraping for industry-specific sources. Owned the full cycle: sales, scoping, build, deployment, handoff.</li>
        </ul>
        <p class="experience-transition">This work led directly to the Data Analyst role at Digi-Tal Regnskab.</p>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Python · n8n · Clay · Apify · HubSpot · GoHighLevel · Excel</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jan to Aug 2023</p>
        <h4 class="experience-role">Marketing &amp; Digital Graduate (student job, part-time during BBA)</h4>
        <p class="experience-company">Damstahl Danmark</p>
        <p class="experience-transition">Part-time student job alongside the BBA at Aarhus BSS.</p>
        <ul class="experience-bullets">
          <li>Product and marketing data in ERP and CRM across European markets.</li>
          <li>Excel dashboards for campaign reporting and standardised regional data processes.</li>
        </ul>
      </div>

    </div>
  </div>
</section>

<section class="cta-soft">
  <div class="container">
    <h2>Hiring, or drowning in Excel?</h2>
    <p class="section-sub">I am open to on-site BI roles in Denmark. Alongside that I take on a few fixed-scope builds for small businesses: from your files to one screen your team trusts.</p>
    <a href="{{ '/contact' | relative_url }}" class="btn-primary">Get in touch →</a>
    <p class="cta-soft-footnote">See my <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a> or grab my CV in <a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" download>English</a> or <a href="{{ '/assets/files/rasmus-kampmann-cv-da.pdf' | relative_url }}" download>Danish</a>.</p>
  </div>
</section>
