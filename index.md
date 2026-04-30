---
layout: home
title: Home
---

<section class="hero">
  <div class="container">
    <span class="eyebrow">RevOps &amp; GTM Engineering</span>
    <h1>I build GTM systems that <span class="highlight">generate pipeline.</span></h1>
    <p class="hero-sub">Outbound automation, lead scoring models, and market intelligence — engineered end-to-end for B2B companies.</p>
    <div class="hero-ctas">
      <a href="#projects" class="btn-primary">See my work</a>
      <a href="/rasmus-krog-revops/contact" class="btn-ghost">Hire me</a>
    </div>
  </div>
</section>

<section class="impact" id="impact">
  <div class="container">
    <p class="section-label">Impact at a glance</p>
    <div class="metrics-grid">
      <div class="metric-card">
        <div class="metric-number">6</div>
        <div class="metric-label">End-to-end GTM systems built</div>
      </div>
      <div class="metric-card">
        <div class="metric-number">110k+</div>
        <div class="metric-label">Companies scored &amp; ranked</div>
      </div>
      <div class="metric-card">
        <div class="metric-number">3</div>
        <div class="metric-label">Production ML models deployed</div>
      </div>
      <div class="metric-card">
        <div class="metric-number">812</div>
        <div class="metric-label">Intelligence sources monitored live</div>
      </div>
    </div>
  </div>
</section>

<section class="skills" id="skills">
  <div class="container">
    <h2>What I build with</h2>
    <p class="section-sub">Grouped by what I actually use them for — not a keyword list.</p>
    <div class="skills-grid">
      <div class="skill-card">
        <div class="skill-icon">🔧</div>
        <h3>Data Engineering</h3>
        <p>Pipelines that pull from APIs, enrich with registries, and land clean data where the team needs it.</p>
        <div class="skill-tags">
          <span class="tag">Python</span><span class="tag">Node.js</span><span class="tag">Airtable</span><span class="tag">Supabase</span><span class="tag">n8n</span><span class="tag">GitHub Actions</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">🤖</div>
        <h3>ML &amp; Lead Scoring</h3>
        <p>Binary classifiers and rule-based scorers that prioritise which accounts to work — trained on real conversion data.</p>
        <div class="skill-tags">
          <span class="tag">XGBoost</span><span class="tag">scikit-learn</span><span class="tag">SHAP</span><span class="tag">pandas</span><span class="tag">propensity modeling</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">📡</div>
        <h3>GTM Automation</h3>
        <p>Outbound sequences, segment routing, and CRM sync — so reps work qualified leads, not spreadsheets.</p>
        <div class="skill-tags">
          <span class="tag">HeyReach</span><span class="tag">Pipedrive</span><span class="tag">Clay</span><span class="tag">LinkedIn automation</span><span class="tag">AI-personalised DMs</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">📊</div>
        <h3>Revenue Analytics</h3>
        <p>Funnel analysis, ICP segmentation, churn timeseries, and cohort retention — built to answer "what's working?"</p>
        <div class="skill-tags">
          <span class="tag">Funnel analysis</span><span class="tag">Cohort</span><span class="tag">ICP segmentation</span><span class="tag">Plotly</span><span class="tag">A/B testing</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">🕸️</div>
        <h3>Scraping &amp; Intelligence</h3>
        <p>Custom scrapers for company registries, social platforms, and news sources — turning the open web into structured signals.</p>
        <div class="skill-tags">
          <span class="tag">Apify</span><span class="tag">FastAPI</span><span class="tag">Playwright</span><span class="tag">OSINT</span><span class="tag">CVR enrichment</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">✨</div>
        <h3>AI Integration</h3>
        <p>Multi-step Claude pipelines that analyse, classify, and write — with structured JSON outputs and retry logic for production.</p>
        <div class="skill-tags">
          <span class="tag">Claude API</span><span class="tag">Prompt engineering</span><span class="tag">Haiku / Sonnet</span><span class="tag">Tool use</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="projects" id="projects">
  <div class="container">
    <h2>Case Studies</h2>
    <p class="section-sub">Real production systems — built, deployed, and measured.</p>
    <div class="projects-grid">
      {% assign sorted_projects = site.projects | sort: "order" %}
      {% for project in sorted_projects %}
        {% include project-card.html project=project %}
      {% endfor %}
    </div>
  </div>
</section>
