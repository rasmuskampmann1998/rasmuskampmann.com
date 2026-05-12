---
layout: home
title: Home
---

<section class="hero">
  <div class="container">
    <div class="hero-text">
      <span class="eyebrow">Data Analyst · BI Developer · AI Workflows</span>
      <h1>I build data, reporting, and AI systems that turn commercial Excel chaos into <span class="highlight">clarity.</span></h1>
      <p class="hero-sub">Data analytics and reporting for B2B commercial teams. SQL, Power BI, Python, and AI workflows built into one system.</p>
      <p class="stack-list">SQL · Power BI · Python · Web Scraping · AI Workflows</p>
      <div class="hero-ctas">
        <a href="{{ '/contact' | relative_url }}" class="btn-primary">Book your free audit →</a>
        <a href="#case-studies" class="btn-ghost">See case studies</a>
      </div>
    </div>
    <div class="hero-portrait">
      {% assign hero_img = '/assets/images/me/hero-portrait.jpg' | relative_url %}
      <img src="{{ hero_img }}" alt="Rasmus Kampmann working" loading="eager" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
    </div>
  </div>
</section>

<section class="who-section">
  <div class="container">
    <span class="eyebrow">Who I work with</span>
    <h2>B2B commercial teams sitting on messy data</h2>
    <p class="who-body">I work with B2B companies whose commercial data lives in too many tools: CRM, spreadsheets, finance systems, and operational tooling that don't talk to each other. The reports take days to build, the numbers don't match, and decisions get made on gut feel instead of evidence. I build the data infrastructure and reporting layer that fixes this.</p>
  </div>
</section>

<section class="impact" id="impact">
  <div class="container">
    <span class="eyebrow">Impact at a glance</span>
    <div class="impact-grid">
      <div class="stat">
        <div class="stat-number">7</div>
        <div class="stat-label">End-to-end data systems shipped</div>
      </div>
      <div class="stat">
        <div class="stat-number">110k+</div>
        <div class="stat-label">Records analysed and scored</div>
      </div>
      <div class="stat">
        <div class="stat-number">3</div>
        <div class="stat-label">Production ML models deployed</div>
      </div>
      <div class="stat">
        <div class="stat-number">812</div>
        <div class="stat-label">External sources monitored live</div>
      </div>
    </div>
  </div>
</section>

<section class="audit-section" id="audit">
  <div class="container">
    <span class="eyebrow">The offer</span>
    <h2>Free Data Audit</h2>
    <p class="section-sub">A written report on your current data setup. What's working, what's not, and the biggest fixes to make. No obligation, no sales call required.</p>

    <div class="audit-grid">
      <div class="audit-left">
        <p>Most B2B teams know their data is messy but can't see where the biggest leaks are. The audit gives you that map.</p>
        <p>After the audit, we discuss whether scoped project work makes sense. There is no productized tier menu. Every engagement is shaped around what the audit surfaces.</p>
        <div class="audit-meta">
          <p><strong>Duration:</strong> 1 to 2 weeks</p>
          <p><strong>For:</strong> Founders, CFOs, and commercial leaders at B2B SMBs</p>
        </div>
        <a href="{{ '/contact' | relative_url }}" class="btn-primary" style="margin-top: 28px;">Request your free audit →</a>
      </div>
      <div class="audit-right">
        <ul class="audit-list">
          <li>Review of your current spreadsheets, reporting, and data flow</li>
          <li>Map of where data lives and where it breaks</li>
          <li>Prioritised list of fixes ranked by impact and effort</li>
          <li>Written PDF you can share with your team</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="projects" id="case-studies">
  <div class="container">
    <span class="eyebrow">Case studies</span>
    <h2>Real systems I built. And the impact they had.</h2>
    <p class="section-sub">Seven production projects across commercial analytics, data infrastructure, ML, and market intelligence. Written for non-technical readers, with full code on GitHub where applicable.</p>
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
    <span class="eyebrow">How I work</span>
    <h2>The delivery methodology behind every engagement</h2>
    <p class="section-sub">Every engagement starts with the free audit. The eight stages below describe the full delivery flow when projects move forward. Not every project touches every stage.</p>

    <ol class="process-steps">
      <li>
        <span class="step-num">01</span>
        <div class="step-body">
          <h4>Free audit of current setup</h4>
          <p>Map the data, spreadsheets, and reporting as they exist today. Identify gaps, brittleness, and the highest-leverage fixes.</p>
        </div>
      </li>
      <li>
        <span class="step-num">02</span>
        <div class="step-body">
          <h4>Data collection &amp; consolidation</h4>
          <p>Pull internal data from CRM, sales, finance, and ops into one clean, joined dataset.</p>
        </div>
      </li>
      <li>
        <span class="step-num">03</span>
        <div class="step-body">
          <h4>Data analysis &amp; insight surfacing</h4>
          <p>Funnel analysis, cohort retention, churn drivers, segment performance. The questions your team has been asking but couldn't answer.</p>
        </div>
      </li>
      <li>
        <span class="step-num">04</span>
        <div class="step-body">
          <h4>Data infrastructure build</h4>
          <p>SQL warehouse, ETL pipelines, a single source of truth that replaces brittle Excel workflows.</p>
        </div>
      </li>
      <li>
        <span class="step-num">05</span>
        <div class="step-body">
          <h4>Reporting &amp; dashboards</h4>
          <p>Power BI dashboards built around the decisions leadership actually makes. Not just the data that happens to be there.</p>
        </div>
      </li>
      <li>
        <span class="step-num">06</span>
        <div class="step-body">
          <h4>AI &amp; automation in the data flow</h4>
          <p>Claude and GPT workflows layered into the pipeline. Classification, enrichment, summarisation. Less manual cleanup.</p>
        </div>
      </li>
      <li>
        <span class="step-num">07</span>
        <div class="step-body">
          <h4>Scraping for external context</h4>
          <p>When internal data isn't enough. Competitor moves, prices, regulations, signals. Custom scrapers feed the same source of truth.</p>
        </div>
      </li>
      <li>
        <span class="step-num">08</span>
        <div class="step-body">
          <h4>AI implementation tied to outcomes</h4>
          <p>Models trained on your data, deployed into the workflows that drive revenue. GTM scoring, financial forecasting, ops optimisation.</p>
        </div>
      </li>
    </ol>
  </div>
</section>

<section class="techstack" id="capabilities">
  <div class="container">
    <span class="eyebrow">Capabilities</span>
    <h2>What I build with</h2>
    <p class="section-sub">The underlying tools, grouped by what I actually use them for.</p>

    <div class="techstack-grid">
      <div class="tech-group">
        <h3>Analysis &amp; modelling</h3>
        <div class="tech-chips">
          <span class="tag">Python</span>
          <span class="tag">pandas</span>
          <span class="tag">scikit-learn</span>
          <span class="tag">XGBoost</span>
          <span class="tag">SHAP</span>
          <span class="tag">Excel</span>
        </div>
      </div>
      <div class="tech-group">
        <h3>Reporting &amp; BI</h3>
        <div class="tech-chips">
          <span class="tag">Power BI</span>
          <span class="tag">DAX</span>
          <span class="tag">Tableau</span>
          <span class="tag">Plotly</span>
          <span class="tag">matplotlib</span>
        </div>
      </div>
      <div class="tech-group">
        <h3>Data infrastructure</h3>
        <div class="tech-chips">
          <span class="tag">PostgreSQL</span>
          <span class="tag">SQL Server</span>
          <span class="tag">Supabase</span>
          <span class="tag">Airtable</span>
          <span class="tag">Node.js</span>
          <span class="tag">ETL pipelines</span>
        </div>
      </div>
      <div class="tech-group">
        <h3>Automation</h3>
        <div class="tech-chips">
          <span class="tag">n8n</span>
          <span class="tag">Make.com</span>
          <span class="tag">GitHub Actions</span>
          <span class="tag">APScheduler</span>
          <span class="tag">Docker</span>
        </div>
      </div>
      <div class="tech-group">
        <h3>Scraping &amp; OSINT</h3>
        <div class="tech-chips">
          <span class="tag">Apify</span>
          <span class="tag">Playwright</span>
          <span class="tag">FastAPI</span>
          <span class="tag">trafilatura</span>
          <span class="tag">CVR / OSINT</span>
        </div>
      </div>
      <div class="tech-group">
        <h3>AI &amp; agentic systems</h3>
        <div class="tech-chips">
          <span class="tag">Claude API</span>
          <span class="tag">MCP</span>
          <span class="tag">OpenAI API</span>
          <span class="tag">Tool use</span>
          <span class="tag">Vibe-code workflows</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="about-strip">
  <div class="container">
    <div class="about-row">
      <div class="about-photo">
        <img src="{{ '/assets/images/me/headshot.jpg' | relative_url }}" alt="Rasmus Kampmann" loading="lazy" />
      </div>
      <div class="about-text">
        <p>Built data and AI systems at Digi-Tal Regnskab and Veginova Seeds. Now freelance, helping B2B SMBs turn commercial data into decisions they can trust.</p>
        <a href="{{ '/about' | relative_url }}">More about me →</a>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Want a free Data Audit?</h2>
    <p>1 to 2 weeks. Written report on your current setup. No obligation, no sales call required.</p>
    <a href="{{ '/contact' | relative_url }}" class="btn-primary">Request your free audit →</a>
  </div>
</section>
