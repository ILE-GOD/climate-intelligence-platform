from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "Daniel_Okom",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="climate_intelligence_pipeline",

    default_args=default_args,

    description="End-to-end climate intelligence data pipeline",

    schedule="0 */6 * * *",

    start_date=datetime(2026, 7, 25),

    catchup=False,

    tags=["climate", "weather", "gcs", "bigquery"],

) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="python /opt/airflow/scripts/extract.py",
        cwd="/opt/airflow",
    )

    validate = BashOperator(
        task_id="validate",
        bash_command="python /opt/airflow/scripts/validate.py",
        cwd="/opt/airflow",
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python /opt/airflow/scripts/transform.py",
        cwd="/opt/airflow",
    )

    feature_engineer = BashOperator(
        task_id="feature_engineer",
        bash_command="python /opt/airflow/scripts/feature_engineering.py",
        cwd="/opt/airflow",
    )

    calculate_risk = BashOperator(
        task_id="calculate_risk",
        bash_command="python /opt/airflow/scripts/calculate_risk.py",
        cwd="/opt/airflow",
    )

    load_to_gcs = BashOperator(
        task_id="load_to_gcs",
        bash_command="python /opt/airflow/scripts/load_to_gcs.py",
        cwd="/opt/airflow",
    )

    load_to_bigquery = BashOperator(
        task_id="load_to_bigquery",
        bash_command="python /opt/airflow/scripts/load_to_bigquery.py",
        cwd="/opt/airflow",
    )


    (
        extract
        >> validate
        >> transform
        >> feature_engineer
        >> calculate_risk
        >> load_to_gcs
        >> load_to_bigquery
    )