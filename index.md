---
layout: home
title: Home
---

<section class="hero">
  <div class="container">
    <span class="eyebrow">Data Analyst · BI Developer · AI Workflows</span>
    <h1>I build data, reporting, and AI systems that turn commercial Excel chaos into <span class="highlight">clarity.</span></h1>
    <p class="hero-sub">Productized engagements for ambitious B2B companies. From a free audit, to a clean data foundation, to AI tied to commercial outcomes.</p>
    <div class="hero-ctas">
      <a href="#offerings" class="btn-primary">See offerings →</a>
      <a href="#case-studies" class="btn-ghost">See case studies</a>
    </div>
  </div>
</section>

<section class="impact" id="impact">
  <div class="container">
    <p class="section-label">Impact at a glance</p>
    <div class="metrics-grid">
      <div class="metric-card">
        <div class="metric-number">7</div>
        <div class="metric-label">End-to-end data systems shipped</div>
      </div>
      <div class="metric-card">
        <div class="metric-number">110k+</div>
        <div class="metric-label">Records analysed and scored</div>
      </div>
      <div class="metric-card">
        <div class="metric-number">3</div>
        <div class="metric-label">Production ML models deployed</div>
      </div>
      <div class="metric-card">
        <div class="metric-number">812</div>
        <div class="metric-label">External sources monitored live</div>
      </div>
    </div>
  </div>
</section>

<section class="offerings" id="offerings">
  <div class="container">
    <p class="section-label">What you can hire me for</p>
    <h2>Three productized offerings</h2>
    <p class="section-sub">Fixed scope. Fixed price. Clear deliverables. Most clients start with the free audit and move into Foundation, then layer AI on top.</p>

    <div class="offerings-grid">

      <a href="{{ '/contact' | relative_url }}" class="offering-card offering-audit">
        <div class="offering-head">
          <span class="offering-tag">Lead-gen offer</span>
          <span class="offering-price">Free</span>
        </div>
        <h3>Data Audit</h3>
        <p class="offering-desc">A written report on your current data setup. What's working, what's not, and the biggest fixes to make. No obligation, no sales call required.</p>
        <ul class="offering-list">
          <li>Review of your current spreadsheets, reporting, and data flow</li>
          <li>Map of where data lives and where it breaks</li>
          <li>Prioritised list of fixes ranked by impact and effort</li>
          <li>Written PDF you can share with your team</li>
        </ul>
        <div class="offering-meta">
          <span><strong>Duration:</strong> 1–2 weeks</span>
          <span><strong>For:</strong> Founders and ops leaders</span>
        </div>
        <span class="offering-cta">Request audit →</span>
      </a>

      <a href="{{ '/contact' | relative_url }}" class="offering-card offering-foundation">
        <div class="offering-head">
          <span class="offering-tag">Main offer</span>
          <span class="offering-price">Fixed price</span>
        </div>
        <h3>Data Foundation</h3>
        <p class="offering-desc">One source of truth and reporting your team actually trusts. Consolidated data infrastructure plus core Power BI dashboards built around the decisions you need to make.</p>
        <ul class="offering-list">
          <li>Data consolidation across CRM, finance, ops, and marketing</li>
          <li>SQL warehouse + ETL pipelines (Supabase / PostgreSQL)</li>
          <li>Core Power BI dashboards for leadership</li>
          <li>Documentation + handover so your team can extend it</li>
        </ul>
        <div class="offering-meta">
          <span><strong>Duration:</strong> 4–8 weeks</span>
          <span><strong>For:</strong> Companies with data in 5+ tools</span>
        </div>
        <span class="offering-cta">Discuss a project →</span>
      </a>

      <a href="{{ '/contact' | relative_url }}" class="offering-card offering-ai">
        <div class="offering-head">
          <span class="offering-tag">Follow-on</span>
          <span class="offering-price">Fixed price</span>
        </div>
        <h3>AI Implementation</h3>
        <p class="offering-desc">A specific AI workflow tied to a commercial outcome. Lead scoring, churn prediction, GTM intelligence, financial forecasting. Models trained on your data, deployed in production.</p>
        <ul class="offering-list">
          <li>Outcome scoped up front (e.g. "lift win rate on outbound by X%")</li>
          <li>Model trained on your real conversion / churn / sales data</li>
          <li>Integration into the workflow where the decision happens</li>
          <li>Monitoring and re-training plan</li>
        </ul>
        <div class="offering-meta">
          <span><strong>Duration:</strong> 4–8 weeks</span>
          <span><strong>For:</strong> Foundation clients ready for layer 2</span>
        </div>
        <span class="offering-cta">Discuss a project →</span>
      </a>

    </div>

    <p class="offerings-note">Looking for ongoing analytics, dashboard maintenance, or new analysis on demand? I offer monthly retainers after a Foundation engagement. <a href="{{ '/contact' | relative_url }}">Get in touch</a>.</p>
  </div>
</section>

<section class="projects" id="case-studies">
  <div class="container">
    <p class="section-label">Case studies</p>
    <h2>Real systems I built. And the impact they had.</h2>
    <p class="section-sub">Seven production projects across GTM, finance, operations, and market intelligence. Written for non-technical readers, with a link to the full code on GitHub.</p>
    <div class="projects-grid">
      {% assign sorted_projects = site.projects | sort: "order" %}
      {% for project in sorted_projects %}
        {% include project-card.html project=project %}
      {% endfor %}
    </div>
  </div>
</section>

<section class="process" id="process">
  <div class="container">
    <p class="section-label">How I work</p>
    <h2>The delivery methodology behind every engagement</h2>
    <p class="section-sub">Whether it's an Audit, a Foundation, or an AI Implementation, the work follows the same eight stages. Not every project touches every stage. This is the underlying flow.</p>

    <ol class="process-steps">
      <li>
        <span class="step-num">01</span>
        <div>
          <h4>Free audit of current setup</h4>
          <p>Map the data, spreadsheets, and reporting as they exist today. Identify gaps, brittleness, and the highest-leverage fixes.</p>
        </div>
      </li>
      <li>
        <span class="step-num">02</span>
        <div>
          <h4>Data collection &amp; consolidation</h4>
          <p>Pull internal data from CRM, sales, finance, and ops into one clean, joined dataset.</p>
        </div>
      </li>
      <li>
        <span class="step-num">03</span>
        <div>
          <h4>Data analysis &amp; insight surfacing</h4>
          <p>Funnel analysis, cohort retention, churn drivers, segment performance. The questions your team has been asking but couldn't answer.</p>
        </div>
      </li>
      <li>
        <span class="step-num">04</span>
        <div>
          <h4>Data infrastructure build</h4>
          <p>SQL warehouse, ETL pipelines, a single source of truth that replaces brittle Excel workflows.</p>
        </div>
      </li>
      <li>
        <span class="step-num">05</span>
        <div>
          <h4>Reporting &amp; dashboards</h4>
          <p>Power BI dashboards built around the decisions leadership actually makes. Not just the data that happens to be there.</p>
        </div>
      </li>
      <li>
        <span class="step-num">06</span>
        <div>
          <h4>AI &amp; automation in the data flow</h4>
          <p>Claude and GPT workflows layered into the pipeline. Classification, enrichment, summarisation. Less manual cleanup.</p>
        </div>
      </li>
      <li>
        <span class="step-num">07</span>
        <div>
          <h4>Scraping for external context</h4>
          <p>When internal data isn't enough. Competitor moves, prices, regulations, signals. Custom scrapers feed the same source of truth.</p>
        </div>
      </li>
      <li>
        <span class="step-num">08</span>
        <div>
          <h4>AI implementation tied to outcomes</h4>
          <p>Models trained on your data, deployed into the workflows that drive revenue. GTM scoring, financial forecasting, ops optimisation.</p>
        </div>
      </li>
    </ol>
  </div>
</section>

<section class="techstack" id="tech-stack">
  <div class="container">
    <p class="section-label">Capabilities</p>
    <h2>What I build with</h2>
    <p class="section-sub">The underlying tools, grouped by what I actually use them for. Listed for credibility, not sold individually.</p>

    <div class="techstack-grid">

      <div class="tech-group">
        <h3>Analysis &amp; modelling</h3>
        <div class="tech-chips">
          <span class="tech-chip">Python</span>
          <span class="tech-chip">pandas</span>
          <span class="tech-chip">scikit-learn</span>
          <span class="tech-chip">XGBoost</span>
          <span class="tech-chip">SHAP</span>
          <span class="tech-chip">Excel</span>
        </div>
      </div>

      <div class="tech-group">
        <h3>Reporting &amp; BI</h3>
        <div class="tech-chips">
          <span class="tech-chip">Power BI</span>
          <span class="tech-chip">DAX</span>
          <span class="tech-chip">Tableau</span>
          <span class="tech-chip">Plotly</span>
          <span class="tech-chip">matplotlib</span>
        </div>
      </div>

      <div class="tech-group">
        <h3>Data infrastructure</h3>
        <div class="tech-chips">
          <span class="tech-chip">PostgreSQL</span>
          <span class="tech-chip">SQL Server</span>
          <span class="tech-chip">Supabase</span>
          <span class="tech-chip">Airtable</span>
          <span class="tech-chip">Node.js</span>
          <span class="tech-chip">ETL pipelines</span>
        </div>
      </div>

      <div class="tech-group">
        <h3>Automation</h3>
        <div class="tech-chips">
          <span class="tech-chip">n8n</span>
          <span class="tech-chip">Make.com</span>
          <span class="tech-chip">GitHub Actions</span>
          <span class="tech-chip">APScheduler</span>
          <span class="tech-chip">Docker</span>
        </div>
      </div>

      <div class="tech-group">
        <h3>Scraping &amp; OSINT</h3>
        <div class="tech-chips">
          <span class="tech-chip">Apify</span>
          <span class="tech-chip">Playwright</span>
          <span class="tech-chip">FastAPI</span>
          <span class="tech-chip">trafilatura</span>
          <span class="tech-chip">CVR / OSINT</span>
        </div>
      </div>

      <div class="tech-group">
        <h3>AI &amp; agentic systems</h3>
        <div class="tech-chips">
          <span class="tech-chip">Claude API</span>
          <span class="tech-chip">MCP</span>
          <span class="tech-chip">OpenAI API</span>
          <span class="tech-chip">Tool use</span>
          <span class="tech-chip">Vibe-code workflows</span>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Want a free Data Audit?</h2>
    <p>1–2 weeks. Written report on your current setup. No obligation, no sales call required.</p>
    <a href="{{ '/contact' | relative_url }}" class="btn-primary-lime">Request my free audit →</a>
  </div>
</section>
