import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from google.cloud import storage

DATA_PROCESSED_DIR = os.environ.get(
    "DATA_PROCESSED_DIR",
    "/opt/airflow/data/processed"
)

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def upload_to_gcs():

    bucket_name = os.getenv("GCS_BUCKET_NAME")

    if not bucket_name:
        raise ValueError(
            "GCS_BUCKET_NAME is not set."
        )

    processed_directory = Path(DATA_PROCESSED_DIR)

    parquet_files = sorted(
        processed_directory.glob("*_risk.parquet")
    )

    if not parquet_files:

        raise FileNotFoundError(
            f"No *_risk.parquet files found in {processed_directory}"
        )

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    uploaded = 0

    for local_file in parquet_files:

        logging.info(
            f"Uploading: {local_file.name}"
        )

        parts = local_file.stem.split("_")

        run_date = next(
            part
            for part in parts
            if part.isdigit() and len(part) == 8
        )

        folder = (
            f"{run_date[:4]}-"
            f"{run_date[4:6]}-"
            f"{run_date[6:8]}"
        )

        destination_blob = (
            f"silver/{folder}/{local_file.name}"
        )

        blob = bucket.blob(
            destination_blob
        )

        blob.upload_from_filename(
            str(local_file)
        )

        logging.info(
            f"Uploaded -> gs://{bucket_name}/{destination_blob}"
        )

        uploaded += 1

    logging.info(
        f"Successfully uploaded {uploaded} files."
    )


if __name__ == "__main__":
    upload_to_gcs()