import logging
from pathlib import Path

from google.cloud import bigquery
from dotenv import load_dotenv
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_gold_tables():

    load_dotenv()

    project_id = os.getenv(
        "BIGQUERY_PROJECT"
    )

    client = bigquery.Client(
        project=project_id
    )

    sql_directory = Path("sql")

    sql_files = [
        "gold_weather_summary.sql",
        "gold_flood_risk.sql",
        "gold_agriculture_advisory.sql",
        "gold_aquaculture_advisory.sql",
        "gold_heat_stress.sql",
        "gold_weather_forecast.sql",
        "gold_rainfall_trends.sql"
    ]

    for sql_file in sql_files:

        logging.info(
            f"Executing {sql_file}..."
        )

        sql_path = (
            sql_directory / sql_file
        )

        query = sql_path.read_text()

        query_job = client.query(
            query
        )

        query_job.result()

        logging.info(
            f"{sql_file} completed successfully."
        )

    logging.info(
        "All Gold tables created successfully."
    )


if __name__ == "__main__":

    create_gold_tables()