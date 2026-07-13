---
layout: home
title: Home
---

<section class="hero-centered">
  <div class="container">
    <div class="hero-avatar">
      <img src="{{ '/assets/images/me/hero-portrait.jpg?v=3' | relative_url }}" alt="Rasmus Kampmann" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
    </div>
    <p class="hero-name">Hi, I'm Rasmus Kampmann</p>
    <h1>Data Analyst | BI Specialist | Power BI Developer</h1>
    <ul class="hero-stack">
      <li>Power BI</li>
      <li>SQL</li>
      <li>Microsoft Fabric</li>
      <li>Python</li>
    </ul>
    <p class="hero-slogan">I turn scattered commercial data into <span class="highlight">systems you can trust.</span></p>
    <p class="hero-background">3+ years working in commercial, now building the reporting a business runs on, and the data foundation AI gets layered on top of. Semantic models, dashboards, forecasting, in agriculture and beyond.</p>
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
    <p class="section-sub">Power BI and SQL are most of the work. The rest is what the work needs.</p>
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
        <p>I build the semantic model first, then the dashboard on top. DAX, Power Query, and a model that stays maintainable, so reporting drives decisions instead of just showing numbers.</p>
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
        <p>I build the data layer that everything else runs on. Data modeling, ETL, PostgreSQL. Raw source data in, analysis-ready tables out, and the team can query them without asking me first.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 2 7 12 12 22 7 12 2"/>
            <polyline points="2 17 12 22 22 17"/>
            <polyline points="2 12 12 17 22 12"/>
          </svg>
        </div>
        <h3>Microsoft Fabric</h3>
        <p>Fabric puts ingestion, modelling, and reporting in one platform instead of three tools that don't talk to each other. I build the SQL and Power BI layer that lands in it. Pipelines and notebooks map straight across from the Postgres and Python stack I run today.</p>
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
        <p>I build the automation and the models spreadsheets can't handle. The ML work runs on scikit-learn and pandas. The pipelines run on a schedule instead of by hand.</p>
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
        <p>Financial modelling belongs in Excel. Forecasts, budgets, margin and customer profitability. KPI definitions that hold across sales, operations, and production.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2l2.5 5.5L20 9l-4 4 1 6-5-3-5 3 1-6-4-4 5.5-1.5z"/>
            <circle cx="12" cy="12" r="1.6"/>
          </svg>
        </div>
        <h3>AI in the data flow</h3>
        <p>AI goes on top of a data foundation, not instead of one. I use Claude Code and Copilot inside the work itself: data prep, SQL and DAX, documentation. A tool in the stack, not the headline.</p>
      </div>

    </div>
  </div>
</section>

<section class="projects is-large" id="projects">
  <div class="container">
    <span class="eyebrow">Explore my work</span>
    <h2>My Projects</h2>
    <p class="section-sub">Production systems behind reporting, forecasting, and commercial decisions. Written for non-technical readers.</p>
    {% assign sorted_projects = site.projects | sort: "order" %}
    <h3 class="lane-title">The reporting a business runs on</h3>
    <p class="lane-sub">Real client systems at an agricultural seed business. One source of truth reconciled to the accounts, and a production plan that stays live instead of going stale on every sale.</p>
    <div class="projects-grid-large">
      {% for project in sorted_projects %}{% if project.lane == 1 %}{% include project-card.html project=project %}{% endif %}{% endfor %}
    </div>
    <h3 class="lane-title">Analysis on a model you can trust</h3>
    <p class="lane-sub">The data model comes before the finding. Star schema in SQL, validated in DuckDB, and only then a number worth acting on. Synthetic data, real method.</p>
    <div class="projects-grid-large">
      {% for project in sorted_projects %}{% if project.lane == 2 %}{% include project-card.html project=project %}{% endif %}{% endfor %}
    </div>
    <h3 class="lane-title">What AI can do once the foundation is there</h3>
    <p class="lane-sub">Both of these are AI sitting on a data layer I had to build first. The registry features and the ingestion corpus are what these models stand on.</p>
    <div class="projects-grid-large">
      {% for project in sorted_projects %}{% if project.lane == 3 %}{% include project-card.html project=project %}{% endif %}{% endfor %}
    </div>
  </div>
</section>

<section class="about-two-col" id="about-strip">
  <div class="container">
    <div class="about-two-col-grid">
      <div class="about-two-col-text">
        <span class="eyebrow">Learn more</span>
        <h2>About Me</h2>
        <p>Hi, I'm Rasmus. I turn scattered commercial data into systems you can trust.</p>
        <p>I build the reporting a business runs on, and the data foundation AI gets layered on top of. One source of truth, semantic models, dashboards, forecasting.</p>
        <p><strong>The problems I get called in for:</strong></p>
        <ul>
          <li>ERP, CRM, and spreadsheet data that don't agree</li>
          <li>KPIs defined differently in every report</li>
          <li>Reporting rebuilt by hand every week</li>
          <li>Forecasting done on gut feel</li>
          <li>AI on the roadmap with no data foundation under it</li>
        </ul>
        <p>My background is in commercial operations, across sales, marketing, finance, and the day-to-day of running a business. That's what sets the work apart: I read the numbers from inside the business, so I know what they mean, where reporting breaks, and how sales, finance, and operations actually use them, because I've worked in those functions, not just reported on them.</p>
        <p>At <strong>Veginova</strong>, an agricultural seed business, I'm building the data, BI, and reporting the business runs on: the finance source of truth, the production planning engine, and the forecasting leadership decides on.</p>
        <p><strong>How I work:</strong></p>
        <ul>
          <li>Build clean, consistent data structures as the foundation</li>
          <li>Automate ingestion and transformation instead of rebuilding manually</li>
          <li>Keep pipelines lightweight, not over-engineered</li>
          <li>Build Power BI models that are easy to maintain and extend</li>
          <li>Build dashboards around the decisions leadership makes</li>
          <li>Use AI inside the data flow, where it makes the work faster or more accurate</li>
        </ul>
        <p><strong>What I've delivered:</strong></p>
        <ul>
          <li>Standardised KPI definitions across sales, operations, and production. Accuracy up 40%+.</li>
          <li>Automated reporting pipelines. 10+ hours of manual work cut per week.</li>
          <li>Forecasting built into a production planning system that sets what to produce, how much, and when.</li>
          <li>Financial data unified into a profitability dashboard, reconciled to the accounts.</li>
        </ul>
        <p style="margin-top: 28px;"><strong>Stack:</strong><br />
        Power BI: semantic models, DAX, Power Query.<br />
        SQL: data modeling, ETL, PostgreSQL.<br />
        Microsoft Fabric: pipelines, Python notebooks for forecasting, Fabric apps.<br />
        Excel: financial modelling, forecasts, budgets, margin.<br />
        AI in the data flow: Claude Code, Copilot, and LLM workflows for data prep, SQL and DAX, and documentation.<br />
        Hands-on across ERPs, CRMs, and spreadsheet/BI tools: the full commercial data layer.</p>
        <p>Most of my experience is from small companies and my own. Close to the decisions, owning the work end to end.</p>
        <p>I replace manual spreadsheets and disconnected reporting with systems that run on their own and make the business easier to understand. The outcome teams hire me for: stop rebuilding reports every Monday, stop questioning the numbers, start making commercial decisions from data you trust.</p>
        <p>Danish, English, Spanish.</p>
        <p><em>Open to data, BI, and Power BI developer roles in Denmark.</em></p>
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
        <p class="experience-date">Jun 2026 – Present · Full-time</p>
        <h4 class="experience-role">Data Analyst &amp; BI Specialist</h4>
        <p class="experience-company">Veginova Seeds</p>
        <ul class="experience-bullets">
          <li>Back at Veginova, building the data, BI, and reporting the business runs on. Extends the reporting stack I already owned here into the financial and operational layer.</li>
          <li>Built the finance source of truth from invoice lines, reconciled to the official accounts, so profit per product and profit per customer are visible for the first time.</li>
          <li>Built the production planning engine that sets what to produce, how much, and when, on a one-year seed lead time. It reproduces the planner's own numbers exactly and lets them test a scenario before committing seed.</li>
          <li>Brought the scoring, forecasting, and revenue analysis I built at Digi-Tal into the finance and operations model here.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> Power BI · SQL · PostgreSQL · Python · Supabase · Claude Code</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Feb 2026 – May 2026 · Full-time · Hybrid</p>
        <h4 class="experience-role">Data Analyst &amp; Commercial Analytics</h4>
        <p class="experience-company">Digi-Tal Regnskab</p>
        <ul class="experience-bullets">
          <li>Owned the data work behind a Danish SMB accounting and fintech firm: ICP, scoring, software detection, and full-channel revenue analysis, from raw source through to operationalised scores feeding sales.</li>
          <li>Built ICP and predictive lead-scoring models plus an ML classifier identifying a prospect's accounting software (holdout AUC 0.75, permutation test p &lt; 0.0001) from Playwright scraping and enrichment waterfalls.</li>
          <li>Full-channel revenue analysis across Meta, Google, LinkedIn outbound, cold calling, and inbound: close rate, conversion, meeting time, and pipeline velocity by channel and segment. Identified which channels drove customers and which burned budget.</li>
          <li>Customer, churn, and attribution analysis: segmented the network into customer, lead, lost, and inactive, and built a full-funnel attribution model joining campaign data, CRM deals, and the Danish business registry to isolate the signals separating payers from non-converters.</li>
          <li>Rebuilt the sales commission model with forecasting weightings, shifting payouts toward subscription and MRR so sellers optimised for LTV instead of discounting to close. Operationalised the scores through an end-to-end LinkedIn pipeline (scraping, enrichment, scoring, sequencing).</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Python · Pipedrive · Clay · Playwright · Apify · HeyReach · Claude</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">May 2025 – Feb 2026 · Full-time · Hybrid</p>
        <h4 class="experience-role">Data Analyst &amp; BI Specialist</h4>
        <p class="experience-company">Veginova Seeds</p>
        <ul class="experience-bullets">
          <li>Owned the BI and reporting stack across sales, operations, and production. Consolidated the source data and stabilised the reporting the team ran on.</li>
          <li>Improved KPI accuracy by 40%+. Standardised metric definitions across teams.</li>
          <li>Cut reporting time by 10+ hours per week. Stabilised broken reporting workflows and consolidated data sources.</li>
          <li>Resolved data inconsistencies across inventory, sales, and production systems.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Power BI · Python · Excel · Clay · Claude Code</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Aug 2023 – May 2025 · Full-time · Hybrid</p>
        <h4 class="experience-role">Marketing Specialist &amp; RevOps</h4>
        <p class="experience-company">Veginova Seeds</p>
        <ul class="experience-bullets">
          <li>B2B marketing and RevOps in agriculture, working with international wholesale, distributor, and grower customers.</li>
          <li>Outbound lead sourcing, CRM hygiene, and lead scoring and prioritisation.</li>
          <li>Trade-fair and grower-event sourcing, pipeline reporting, and channel attribution.</li>
        </ul>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jun 2024 – Aug 2025 · Self-employed · Remote</p>
        <h4 class="experience-role">Founder · Data &amp; RevOps</h4>
        <p class="experience-company">Sira Logic</p>
        <ul class="experience-bullets">
          <li>Service business building AI-driven lead generation, enrichment, and CRM automation for B2B companies.</li>
          <li>Built lead enrichment and scoring workflows. Qualification accuracy improved by 30–40%.</li>
          <li>Built CRM automation pipelines integrating HubSpot and GoHighLevel with external data sources.</li>
          <li>Built custom web scraping systems for industry-specific data sources.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Python · Clay · Apify · HubSpot · GoHighLevel · HeyReach</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jan 2025 – Jan 2026 · Freelance · Remote</p>
        <h4 class="experience-role">AI &amp; LLM Data Analyst</h4>
        <p class="experience-company">Outlier</p>
        <ul class="experience-bullets">
          <li>Reviewed and annotated 1,000+ Danish-language AI conversations to improve response quality.</li>
          <li>Spotted patterns where models failed and fed that back into training data.</li>
          <li>Built practical understanding of how LLMs work and where they break. The same insight powers the AI scoring and qualification workflows I build today.</li>
        </ul>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jan 2023 – Aug 2023 · Part-time · Hybrid</p>
        <h4 class="experience-role">Marketing &amp; Digital Graduate</h4>
        <p class="experience-company">Damstahl Danmark</p>
        <ul class="experience-bullets">
          <li>Managed product and marketing data in ERP and CRM platforms across European markets.</li>
          <li>Built Excel dashboards for campaign reporting.</li>
          <li>Standardised regional data processes.</li>
        </ul>
      </div>

    </div>
  </div>
</section>

<section class="cta-soft">
  <div class="container">
    <span class="eyebrow">Want to work together?</span>
    <h2>See my freelance services</h2>
    <a href="{{ '/services' | relative_url }}" class="btn-primary">View Services →</a>
    <p class="cta-soft-footnote">Recruiters: see my <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a> or grab my CV in <a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" download>English</a> or <a href="{{ '/assets/files/rasmus-kampmann-cv-da.pdf' | relative_url }}" download>Danish</a>.</p>
  </div>
</section>
