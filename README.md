# Market Forecasting & Media Mix Decision Engine

> **End-to-end portfolio project** - from market-level sales forecasting to media mix modeling and budget allocation recommendations. Designed to reflect the analytical depth expected of senior Data Scientists and Data Engineers working in marketing, growth, or commercial strategy.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Airflow](https://img.shields.io/badge/Airflow-2.x-017CEE?logo=apache-airflow)
![MLflow](https://img.shields.io/badge/MLflow-Tracking%20%26%20Registry-0194E2?logo=mlflow)
![FastAPI](https://img.shields.io/badge/FastAPI-Serving-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![Great Expectations](https://img.shields.io/badge/Great%20Expectations-Data%20Quality-FF6B35)
![Evidently](https://img.shields.io/badge/Evidently-Drift%20Monitoring-9C27B0)

---

## Business Problem

Marketing and growth teams routinely make critical decisions under uncertainty: *Which markets deserve more investment? What media mix maximizes incremental revenue? What is the expected ROI of this campaign?*

This platform builds an **analytical decision-support framework** that goes beyond descriptive reporting:

- **Where to invest** - market-level sales forecasting with trend and seasonality decomposition
- **What mix to use** - Media Mix Modeling to estimate the incremental contribution of each channel
- **How to allocate** - scenario simulation and budget optimization across markets and channels
- **Whether it worked** - uplift modeling and incrementality measurement to validate causal impact

The project is built on the public **[Store Item Demand Forecasting](https://www.kaggle.com/c/demand-forecasting-kernels-only)** dataset (daily sales at store-item level), enriched with a synthetic-but realistic-marketing layer to enable full MMM and uplift analysis.

---

## What This Project Demonstrates

| Capability | Details |
|---|---|
| **Time Series Forecasting** | Sales forecasting at market level; trend, seasonality, and store/item hierarchy handling |
| **Market Aggregation** | Store → market rollup (daily → weekly/monthly), normalized for cross-market comparison |
| **Media Mix Modeling** | Adstock transformations, Hill saturation curves, channel contribution decomposition, ROI estimation |
| **Uplift Modeling** | Heterogeneous treatment effects - S-learner, T-learner, meta-learner approaches |
| **Budget Optimization** | Marginal return curves, scenario analysis, channel budget reallocation recommendations |
| **Causal Inference** | Counterfactual design, synthetic treatment/control assignment, incrementality validation |
| **Data Engineering** | Multi-source ingestion pipelines, synthetic data generation, feature versioning |
| **MLOps** | Experiment tracking, model registry, batch + API serving, monitoring and drift detection |
| **Data Quality** | Schema validation (Great Expectations), drift monitoring (Evidently AI), data contracts |
| **Software Engineering** | Modular src layout, unit & integration tests, synthetic fixtures, Docker, config management |

---

## Tech Stack

| Layer | Tools |
|---|---|
| **MMM / Causal** | PyMC · LightweightMMM · scikit-learn |
| **Uplift** | Meta-learners (S/T/X) · two-model approach |
| **Feature Engineering** | pandas · numpy · custom adstock & saturation modules |
| **Orchestration** | Apache Airflow 2.x (7 production DAGs) |
| **Experiment Tracking** | MLflow (runs, registry, artifact storage) |
| **Serving** | FastAPI · Docker (Dockerfile.api) |
| **Data Quality** | Great Expectations · Evidently AI |
| **Testing** | pytest · synthetic CSV fixtures |
| **Config** | YAML-based (dev / prod profiles) · python-dotenv |
| **Infrastructure** | Docker Compose · Makefile |

---

## Architecture Overview

```
Store Item Demand Data (Kaggle)  +  Synthetic Marketing Layer
            │                              │
            └──────────────┬──────────────┘
                           ▼
            ┌──────────────────────────────┐
            │   Ingestion & Validation      │  ← sales_ingestion_dag
            │   Great Expectations checks   │    marketing_ingestion_dag
            └──────────────┬───────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │   Feature Engineering         │  ← feature_pipeline_dag
            │   Adstock · Saturation        │    adstock.py · lag_features.py
            │   Calendar · Panel build      │    calendar_features.py
            └──────────────┬───────────────┘
                           │
              ┌────────────┴─────────────┐
              ▼                          ▼
  ┌─────────────────────┐   ┌────────────────────────┐
  │   MMM Training       │   │   Uplift Training       │
  │   Bayesian · Ridge   │   │   Meta-learners         │  ← MLflow tracking
  │   Baseline           │   │   Two-model approach    │
  └──────────┬──────────┘   └───────────┬────────────┘
             │                          │
             └─────────────┬────────────┘
                           ▼
            ┌──────────────────────────────┐
            │   Evaluation & Attribution    │  ← scoring_and_budget_dag
            │   ROI decomp · AUUC · Qini   │
            └──────────────┬───────────────┘
                           │
              ┌────────────┴─────────────┐
              ▼                          ▼
  ┌─────────────────────┐   ┌────────────────────────┐
  │   Budget Optimizer   │   │   FastAPI Endpoint      │
  │   Scenario analysis  │   │   /recommend            │
  │   Marginal returns   │   │   RecommendationResponse│
  └─────────────────────┘   └────────────────────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │   Monitoring                  │  ← monitoring_dag
            │   Evidently drift · Alerts    │
            └──────────────────────────────┘
```

---

## Project Structure

```
marketing-investments-optimization/
│
├── airflow/
│   └── dags/
│       ├── sales_ingestion_dag.py
│       ├── marketing_ingestion_dag.py
│       ├── feature_pipeline_dag.py
│       ├── mmm_training_dag.py
│       ├── uplift_training_dag.py
│       ├── scoring_and_budget_dag.py
│       └── monitoring_dag.py
│
├── api/
│   ├── app.py                       # FastAPI application
│   ├── model_loader.py              # MLflow model loading
│   └── schemas.py                   # RecommendationRequest / Response
│
├── src/
│   ├── ingestion/                   # Data loading (sales + marketing)
│   ├── preprocessing/               # Panel build, cleaning
│   ├── features/
│   │   ├── adstock.py               # Geometric & Weibull adstock
│   │   ├── saturation.py            # Hill saturation curves
│   │   ├── lag_features.py          # Temporal lag engineering
│   │   ├── calendar_features.py     # Seasonality features
│   │   ├── build_mmm_featureset.py
│   │   └── build_uplift_dataset.py
│   ├── training/
│   │   ├── train_bayesian_mmm.py    # PyMC / LightweightMMM
│   │   ├── train_mmm_baseline.py
│   │   ├── train_ridge_mmm.py
│   │   ├── train_uplift_meta_learners.py
│   │   └── train_uplift_two_model.py
│   ├── evaluation/
│   │   ├── mmm_metrics.py           # MAPE, SMAPE, WMAPE, Holdout R²
│   │   ├── uplift_metrics.py        # AUUC, Qini, uplift@k
│   │   ├── attribution_analysis.py
│   │   └── policy_evaluation.py
│   ├── optimization/
│   │   ├── budget_allocation.py     # Marginal return optimization
│   │   └── channel_scenario_analysis.py
│   ├── inference/
│   │   ├── mmm_scoring.py
│   │   ├── uplift_scoring.py
│   │   └── recommendation_service.py
│   ├── monitoring/
│   │   ├── drift.py                 # Evidently AI integration
│   │   ├── data_quality.py
│   │   └── alerts.py
│   ├── simulation/
│   │   ├── generate_marketing_data.py   # Synthetic spend/impressions
│   │   └── simulate_treatment_assignment.py
│   └── pipelines/                   # Orchestration glue code
│
├── quality/
│   ├── great_expectations/          # Expectation suites for raw data
│   └── evidently/                   # Drift config
│
├── notebooks/
│   ├── 01_sales_eda.md
│   ├── 02_marketing_layer_design.md
│   ├── 03_feature_design.md
│   ├── 04_mmm_results.md
│   ├── 05_uplift_results.md
│   └── 06_budget_allocation_strategy.md
│
├── tests/
│   ├── unit/                        # Schema, config, placeholder tests
│   ├── integration/                 # Import checks, API health
│   └── fixtures/                    # sample_sales_small.csv · sample_marketing_small.csv
│
├── docs/
│   ├── architecture.md
│   ├── business_case.md
│   ├── dataset_strategy.md
│   ├── governance.md
│   ├── implementation_plan_6_weeks.md
│   ├── testing_strategy.md
│   └── model_card_template.md
│
├── configs/
│   ├── base.yaml
│   ├── dev.yaml
│   ├── prod.yaml
│   └── model_config.yaml
│
├── scripts/
│   ├── generate_synthetic_marketing.py
│   ├── run_mmm_train.py
│   ├── run_uplift_train.py
│   ├── run_scoring.py
│   └── generate_reports.py
│
├── Dockerfile.api
├── docker-compose.yml
├── Makefile
├── pyproject.toml
└── requirements.txt
```

---

## Key Design Decisions

**Synthetic marketing layer over waiting for real data.** Real datasets for MMM rarely exist in public form. The simulation module generates realistic spend curves, channel seasonality, and treatment assignment - enabling full methodology demonstration without relying on proprietary data, while keeping the workflow production-equivalent.

**Multiple MMM training approaches.** Three implementations are included: Bayesian (uncertainty quantification via PyMC/LightweightMMM), Ridge regression (fast baseline), and a structural baseline. This allows honest comparison and reflects real-world model selection processes.

**Meta-learner uplift + two-model approach.** Rather than picking one uplift framework, both S/T/X meta-learners and the two-model approach are implemented. This reflects the practical reality that heterogeneous treatment effect estimation is not solved by a single algorithm.

**Optimization as a first-class module.** The `src/optimization/` layer translates model outputs into actionable budget decisions - marginal return curves, channel scenario analysis, reallocation recommendations. This is the business-facing output that makes MMM operationally useful.

**FastAPI recommendation endpoint.** Model serving is not an afterthought. A typed REST endpoint (`RecommendationRequest / RecommendationResponse`) exposes MMM and uplift model outputs for integration with downstream systems.

**Monitoring from day one.** Evidently AI drift config and alert modules are built into the architecture, reflecting that distribution shift is the dominant failure mode for models deployed over time.

---

## Data Policy

| What | Status |
|---|---|
| Source code, DAGs, configs | ✅ Versioned |
| Tests & synthetic fixtures | ✅ Versioned |
| Notebooks & documentation | ✅ Versioned |
| Model card template | ✅ Versioned |
| Raw CSVs, model binaries | ❌ Git-ignored |
| Credentials / secrets | ❌ `.env` (see `.env.example`) |

Raw data must be downloaded manually from [Kaggle](https://www.kaggle.com/c/demand-forecasting-kernels-only) and placed in `data/raw/sales/`. A synthetic marketing layer can be generated via `scripts/generate_synthetic_marketing.py`.

---

## Quickstart

```bash
# 1. Clone and configure
git clone <repo-url> && cd marketing-investments-optimization
cp .env.example .env

# 2. Set up environment
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. Start infrastructure (Airflow + MLflow)
docker compose up -d

# 4. Download Kaggle data and place in data/raw/sales/
#    Or generate synthetic marketing layer:
python scripts/generate_synthetic_marketing.py

# 5. Run tests
make test

# 6. Train MMM
python scripts/run_mmm_train.py

# 7. Start the recommendation API
docker build -f Dockerfile.api -t mmm-api . && docker run -p 8000:8000 mmm-api
```

---

## Model Evaluation Metrics

| Model | Metrics |
|---|---|
| **MMM** | MAPE · SMAPE · WMAPE · Holdout R² |
| **Uplift** | AUUC · Qini coefficient · uplift@k |
| **Budget Optimization** | Marginal return per channel · Incremental revenue · ROI |

---

## Documentation

- [`docs/business_case.md`](docs/business_case.md) - Problem framing and strategic objectives
- [`docs/architecture.md`](docs/architecture.md) - System design and component interactions
- [`docs/dataset_strategy.md`](docs/dataset_strategy.md) - Data sourcing and synthetic layer design
- [`docs/implementation_plan_6_weeks.md`](docs/implementation_plan_6_weeks.md) - Phased delivery plan
- [`docs/testing_strategy.md`](docs/testing_strategy.md) - Testing approach and maintainability rationale
- [`docs/governance.md`](docs/governance.md) - Data governance and model accountability
- [`docs/model_card_template.md`](docs/model_card_template.md) - Structured model documentation template
