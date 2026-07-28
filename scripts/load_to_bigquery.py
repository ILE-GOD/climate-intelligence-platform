import logging
from google.cloud import bigquery

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Configuration
PROJECT_ID = "capable-avatar-475900-j5"
DATASET_ID = "climate_gold"
TABLE_ID = "weather_risk"

GCS_URI = (
    "gs://climate-intel-raw-data-2026/"
    "silver/2026-07-25/weather_risk.parquet"
)


def load_to_bigquery():

    logging.info(
        "Starting BigQuery load..."
    )

    # Create BigQuery client
    client = bigquery.Client(
        project=PROJECT_ID
    )

    # Create dataset if it does not exist
    dataset_ref = f"{PROJECT_ID}.{DATASET_ID}"

    dataset = bigquery.Dataset(
        dataset_ref
    )

    dataset.location = "africa-south1"

    client.create_dataset(
        dataset,
        exists_ok=True
    )

    logging.info(
        f"Dataset ready: {dataset_ref}"
    )

    # Define explicit schema
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

    # Configure load job
    table_ref = (
        f"{PROJECT_ID}."
        f"{DATASET_ID}."
        f"{TABLE_ID}"
    )

    job_config = bigquery.LoadJobConfig(

        source_format=(
            bigquery.SourceFormat.PARQUET
        ),

        schema=schema,

        write_disposition=(
            bigquery.WriteDisposition
            .WRITE_TRUNCATE
        )
    )

    logging.info(
        f"Loading data from: {GCS_URI}"
    )

    # Load Parquet from GCS into BigQuery
    load_job = client.load_table_from_uri(

        GCS_URI,

        table_ref,

        job_config=job_config
    )

    # Wait for job to finish
    load_job.result()

    logging.info(
        "Data loaded successfully!"
    )

    logging.info(
        f"BigQuery table: {table_ref}"
    )


if __name__ == "__main__":

    load_to_bigquery()