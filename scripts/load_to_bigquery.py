import logging
import os

from google.cloud import bigquery
from google.cloud import storage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

PROJECT_ID = os.getenv("BIGQUERY_PROJECT")
DATASET_ID = "climate_gold"
TABLE_ID = "weather_risk"

BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")


def get_latest_gcs_file():
    """
    Returns the newest risk parquet file in GCS.
    """

    storage_client = storage.Client()

    bucket = storage_client.bucket(BUCKET_NAME)

    blobs = list(bucket.list_blobs(prefix="silver/"))

    parquet_files = [
        blob
        for blob in blobs
        if blob.name.endswith("_risk.parquet")
    ]

    if not parquet_files:
        raise FileNotFoundError(
            "No risk parquet file found in GCS."
        )

    latest_blob = max(
        parquet_files,
        key=lambda blob: blob.time_created
    )

    logging.info(
        f"Latest GCS file: {latest_blob.name}"
    )

    return f"gs://{BUCKET_NAME}/{latest_blob.name}"


def load_to_bigquery():

    logging.info(
        "Starting BigQuery load..."
    )

    client = bigquery.Client(
        project=PROJECT_ID
    )

    # --------------------------------------------------
    # Create dataset if it doesn't exist
    # --------------------------------------------------

    dataset_ref = f"{PROJECT_ID}.{DATASET_ID}"

    dataset = bigquery.Dataset(dataset_ref)

    dataset.location = "africa-south1"

    client.create_dataset(
        dataset,
        exists_ok=True
    )

    logging.info(
        f"Dataset ready: {dataset_ref}"
    )

    # --------------------------------------------------
    # Schema
    # --------------------------------------------------

    schema = [

        bigquery.SchemaField(
            "date",
            "DATE"
        ),

        bigquery.SchemaField(
            "temperature_max",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "temperature_min",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "precipitation_mm",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "location",
            "STRING"
        ),

        bigquery.SchemaField(
            "latitude",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "longitude",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "extracted_at",
            "TIMESTAMP"
        ),

        bigquery.SchemaField(
            "rainfall_3_day_total",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "rainfall_7_day_total",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "temperature_change",
            "FLOAT"
        ),

        bigquery.SchemaField(
            "flood_risk",
            "STRING"
        ),

        bigquery.SchemaField(
            "sustained_flood_risk",
            "STRING"
        ),

        bigquery.SchemaField(
            "soil_saturation_risk",
            "STRING"
        ),

        bigquery.SchemaField(
            "crop_stress",
            "STRING"
        ),

        bigquery.SchemaField(
            "pond_overflow_risk",
            "STRING"
        ),
    ]

    table_ref = (
        f"{PROJECT_ID}."
        f"{DATASET_ID}."
        f"{TABLE_ID}"
    )

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        write_disposition="WRITE_APPEND",
        schema=schema,
        schema_update_options=[
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION
        ]
    )

    # --------------------------------------------------
    # Find newest file in GCS
    # --------------------------------------------------

    gcs_uri = get_latest_gcs_file()

    logging.info(
        f"Loading data from: {gcs_uri}"
    )

    load_job = client.load_table_from_uri(
        gcs_uri,
        table_ref,
        job_config=job_config
    )

    load_job.result()

    logging.info(
        "Data loaded successfully."
    )

    # --------------------------------------------------
    # Remove duplicates
    # --------------------------------------------------

    logging.info(
        "Removing duplicate records..."
    )

    query = f"""
    CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}` AS
    SELECT * EXCEPT(row_num)
    FROM (
        SELECT *,
            ROW_NUMBER() OVER(
                PARTITION BY
                    date,
                    location,
                    extracted_at
                ORDER BY extracted_at DESC
            ) AS row_num
        FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
    )
    WHERE row_num = 1
    """

    client.query(query).result()

    logging.info(
        "Duplicate removal completed."
    )

    logging.info(
        f"BigQuery table ready: {table_ref}"
    )


if __name__ == "__main__":
    load_to_bigquery()