import logging
import os
from pathlib import Path
from datetime import date

from dotenv import load_dotenv
from google.cloud import storage
import os

DATA_PROCESSED_DIR = os.environ.get("DATA_PROCESSED_DIR", "/opt/airflow/data/processed")

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def upload_to_gcs():
    # Get configuration from .env
    bucket_name = os.getenv("GCS_BUCKET_NAME")

    if not bucket_name:
        raise ValueError("GCS_BUCKET_NAME is not set in the .env file.")

    # Local Silver-layer file
    local_file = Path("data/processed/weather_risk.parquet")

    if not local_file.exists():
        raise FileNotFoundError(f"File not found: {local_file}")

    # Date-based folder
    today = date.today().isoformat()

    # Destination inside GCS
    destination_blob = f"silver/{today}/weather_risk.parquet"

    logging.info(f"Uploading {local_file}...")

    # Create GCS client
    storage_client = storage.Client()

    # Get bucket
    bucket = storage_client.bucket(bucket_name)

    # Create blob
    blob = bucket.blob(destination_blob)

    # Upload file
    blob.upload_from_filename(str(local_file))

    logging.info("File uploaded successfully!")
    logging.info(f"Location: gs://{bucket_name}/{destination_blob}")


if __name__ == "__main__":
    upload_to_gcs()