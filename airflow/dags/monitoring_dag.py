"""DAG placeholder: monitoring_dag."""
from datetime import datetime

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except Exception:  # pragma: no cover
    DAG = object
    PythonOperator = object


def _placeholder_task(**kwargs):
    print("TODO: conectar lógica real")


def build_dag():
    default_args = {"owner": "abel.soto", "retries": 1}
    dag = DAG(
        dag_id="monitoring_dag",
        default_args=default_args,
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
        tags=["marketing", "mmm", "uplift"],
    )
    step_1 = PythonOperator(task_id="step_1", python_callable=_placeholder_task, dag=dag)
    step_2 = PythonOperator(task_id="step_2", python_callable=_placeholder_task, dag=dag)
    step_1 >> step_2
    return dag


dag = build_dag()
