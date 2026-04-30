---
layout: project
title: Accounting Software Propensity Model
tagline: "XGBoost binary classifier predicting which SMBs are most likely to switch to e-conomic — AUC 0.747"
tools: [Python, XGBoost, scikit-learn, SHAP, pandas]
outcome_headline: "4,658 companies scored — top decile converts at 3× the baseline rate"
outcome_detail: "Deployed into production lead scoring as a +15 point signal bonus. Continuously improves as new labelled deals are added."
order: 2
cover_emoji: "🤖"
---

## The Problem

Not all leads are equal — but without a model, the pipeline treated a company using e-conomic (high propensity to become a client) the same as one using a competing system they were deeply embedded in. The goal was to identify, from publicly available company data alone, which SMBs were *most likely* to be running e-conomic accounting software — and therefore most likely to convert.

## Feature Engineering

The model uses eight features derived entirely from the Danish company registry (CVR) and industry codes — no enrichment vendor required:

| Feature | Source | Why It Matters |
|---------|--------|---------------|
| `company_form` | CVR | ApS/IVS firms use e-conomic at higher rates than sole traders |
| `emp_band` | CVR | 2–10 employee band is the sweet spot |
| `vat_frequency` | CVR | Quarterly VAT filers correlate with software adoption |
| `company_age` | CVR | Newer companies (< 5 years) over-index on e-conomic |
| `industry` (5 binary flags) | NACE code | IT, mgmt consulting, media, trade, construction |
| `has_revisor` | Proff.dk scrape | Companies with an auditor are more structured — higher adoption |

```python
# Sanitised feature engineering — applied to all three data sources
def apply_features(df, age_col, vat_col, emp_col, form_col, ind_col, **kwargs):
    """Engineer model features from raw CVR / Pipedrive columns."""

    # Company age in years
    if age_col and age_col in df.columns:
        df['company_age'] = (
            pd.Timestamp.now().year -
            pd.to_datetime(df[age_col], errors='coerce').dt.year
        ).clip(0, 50)

    # Employee band → numeric midpoint
    EMP_MAP = {'0-1': 0.5, '2-4': 3, '5-9': 7, '10-19': 14,
               '20-49': 34, '50+': 60}
    if emp_col and emp_col in df.columns:
        df['emp_band_num'] = df[emp_col].map(EMP_MAP).fillna(5)

    # VAT frequency → ordinal
    VAT_MAP = {'Månedlig': 12, 'Kvartal': 4, 'Halvår': 2, 'Årsvis': 1}
    if vat_col and vat_col in df.columns:
        df['vat_freq_num'] = df[vat_col].map(VAT_MAP).fillna(4)

    # Company form one-hot
    FORM_MAP = {'ApS': 0, 'IVS': 1, 'A/S': 2, 'ENK': 3, 'I/S': 4}
    if form_col and form_col in df.columns:
        df['form_code'] = df[form_col].map(FORM_MAP).fillna(5)

    return df
```

## Training Setup

Three data sources are combined for training: Pipedrive won deals (ground truth), Adversus company database (110k firms with accounting system labels), and a held-out ICP master set for unbiased evaluation.

```python
# Binary target: e-conomic = 1, everything else = 0
train_df['label'] = (train_df['software'] == 'e-conomic').astype(int)

xgb = XGBClassifier(
    n_estimators=400, max_depth=5, learning_rate=0.05,
    subsample=0.8, colsample_bytree=0.8,
    scale_pos_weight=non_count / ec_count,  # handle class imbalance
    eval_metric='logloss', random_state=42, n_jobs=-1
)

# 5-fold stratified CV — report CV AUC before touching holdout
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_probs = cross_val_predict(xgb, X_train, y_train, cv=cv, method='predict_proba')
cv_auc   = roc_auc_score(y_train, cv_probs[:, 1])

print(f"CV AUC:        {cv_auc:.3f}")   # → 0.741
print(f"Holdout AUC:   {test_auc:.3f}") # → 0.747
```

The model is validated against a 200-shuffle permutation test to confirm the AUC is significantly above chance (p < 0.05).

## SHAP Explainability

SHAP values make the model's decisions auditable — important when using scores to justify outreach prioritisation:

```python
explainer = shap.TreeExplainer(xgb)
sv = explainer.shap_values(X_shap)

# Top features by mean absolute SHAP value
# company_age:   0.0821  ████████
# emp_band_num:  0.0614  ██████
# form_code:     0.0531  █████
# has_revisor:   0.0487  ████
# vat_freq_num:  0.0392  ████
```

Younger companies with 2–9 employees in an ApS structure, with a registered auditor, score highest — consistent with the client profile observed in won deals.

## Production Integration

The model runs as a scoring step in the outbound pipeline. Scores are pre-computed for all 110k companies and stored as a lookup CSV:

```python
# Threshold: prob >= 0.50 → +15 signal bonus in lead scoring
dim['prob_economic'] = xgb.predict_proba(X_score)[:, 1]
dim['econ_signal']   = (dim['prob_economic'] >= 0.50).astype(int) * 15
```

The `--add-label` flag lets new labelled leads from Pipedrive be added to the training set, and `--retrain` rebuilds the model — a continuous feedback loop as the pipeline generates more conversion data.

## Results

<div class="result-box">
  <div class="result-label">Model Performance</div>
  <ul>
    <li>Holdout AUC: <strong>0.747</strong> — significantly above chance (permutation p &lt; 0.05)</li>
    <li>Training set: 4,658 labelled companies across 3 sources</li>
    <li>Top decile precision: ~3× baseline conversion rate</li>
    <li>+15 pts signal bonus integrated into production lead scoring</li>
    <li>Continuous retraining loop as new Pipedrive deals are won</li>
  </ul>
</div>

## Key Lessons

**Use all available labelled data.** Combining CRM deals with the company database gave 4× more training examples than using deals alone, without needing external enrichment.

**Explainability earns trust.** SHAP values let non-technical stakeholders understand *why* a company scored high — which was critical for buy-in when the model was deployed to influence sales priorities.

**Keep the feedback loop tight.** A model trained once and never updated degrades. The `--retrain` flag makes retraining a 30-second operation, not a project.
