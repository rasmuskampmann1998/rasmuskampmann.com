---
layout: project
title: Software Detection ML Model
tagline: "A binary classifier that predicts software adoption from public company-registry features alone. Statistics, modelling, and deployment from scratch."
tools: [Python, scikit-learn, XGBoost, SHAP, pandas, PostgreSQL]
outcome_headline: "A simple set of public features predicts adoption well enough to prioritise outbound at the top of the funnel"
outcome_detail: "Trained, evaluated, calibrated, deployed as a score boost in the lead-scoring system. Reproducible on a 5,000-row synthetic dataset."
order: 5
cover_image: /assets/images/projects/software-detection-ml.jpg
github_url: https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies/tree/main/03-software-detection-ml
---

## The question

A B2B sales team wanted to prioritise outbound towards companies that already use a specific piece of accounting software, on the hypothesis that those companies are cheaper to win as customers because the friction to switch is lower. There was no list. Data vendors that track this for small companies charge too much to use at the top of a cold-outbound funnel.

The question: can the label be predicted from public Danish company-registry data alone, well enough to reorder a dialler queue?

## Data modelling

Before any modelling, the data model itself had to be right. I designed a single flat training table joined from:

- The public CVR registry (company form, founding date, employee band, VAT cadence, industry NACE code, region)
- The CRM's labelled outcomes (companies known to use the target software, companies known to use a named competitor)

The schema is normalised: each row is one company, one label, one timestamp. No duplicates, no leaks of future information into past records. Categorical columns are typed as enums, not free text, so the same value can't accidentally appear in five spellings.

## Statistical setup

Before training I checked the basics:

- **Class balance.** Positive class around 50%, no need for class weighting.
- **Feature distributions.** Histograms per feature to spot data-entry mistakes and outliers.
- **Bivariate signal.** Chi-square tests between each categorical feature and the label to confirm at least some columns carry predictive information before spending model-training time.
- **Train-test split.** Stratified 80/20, fixed seed, no leakage between sets.

## The model

XGBoost binary classifier. Categorical features one-hot encoded, `founded_year` converted to `company_age`, `has_subsidiaries` cast to integer. The model trains in seconds on five thousand rows; the production version trains in a couple of minutes on the real labelled set.

Why XGBoost over a regression. Logistic regression assumes additive log-odds and handles interactions only with manual feature engineering. Tree ensembles pick up the interactions naturally and tolerate the mix of categorical and numeric features. I tried both. The tree ensemble landed roughly 5 AUC points higher on the same holdout.

## Evaluation

I evaluated the model at five levels, not just AUC:

- **ROC curve and AUC.** Holdout AUC sits in the 0.74 to 0.78 range. Mirrors what models on this kind of problem typically achieve.
- **Confusion matrix at the 0.5 threshold.** Confirms that the false-positive rate is acceptable for downstream use.
- **Precision-recall curve.** Useful because the operational question is "if I act on the top decile, how many of those are right?".
- **Probability calibration.** Calibration plot to confirm that a score of 0.7 actually means roughly a 70% positive rate. If the model isn't calibrated, the +score boost downstream would be miscalibrated too.
- **Feature importance with SHAP.** Top-15 features by SHAP value, plus per-prediction explanations for the sales team's edge cases.

The top features are unsurprising on their own. Employee band, company form, VAT cadence, industry, company age. The interesting part is how they combine: a new private-limited with five employees filing quarterly VAT in an IT-adjacent industry scores very differently from a twenty-year-old sole trader in trades.

## Threshold selection and deployment

Picking 0.5 is the default, but not always the right call. I chose the operational threshold by plotting top-decile precision and the marginal lift over baseline at each threshold, then picked the one that maximised expected revenue uplift per dial.

The output plugs directly into the lead-scoring system. Companies above threshold get a score boost before they reach the dialler queue. Retraining is monthly, triggered by a GitHub Actions workflow that fires when new labelled outcomes arrive in the CRM.

## How it gets used

The model doesn't replace the outbound team. It reorders the queue. Reps work the same lead types. They start their week on the companies the model thinks are most likely to fit, which compounds over the quarter.

## Tools

Python, pandas, scikit-learn for the data work. XGBoost for the model. SHAP for explainability. PostgreSQL for the training-data warehouse. GitHub Actions for the monthly retraining cron. The public version trains on a synthetic 5,000-row CVR-style dataset that's regenerable from a single script.
