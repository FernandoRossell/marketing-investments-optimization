# Diseño de DAGs de Airflow

## Principios
- Los DAGs solo definen orquestación.
- La lógica pesada vive en `src/` y `scripts/`.
- Tareas atómicas y reejecutables.

## DAGs incluidos
- `sales_ingestion_dag`
- `marketing_ingestion_dag`
- `feature_pipeline_dag`
- `mmm_training_dag`
- `uplift_training_dag`
- `scoring_and_budget_dag`
- `monitoring_dag`
