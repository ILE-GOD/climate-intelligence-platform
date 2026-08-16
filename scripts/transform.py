import json
import logging
from pathlib import Path

import pandas as pd
import os

DATA_RAW_DIR = os.environ.get("DATA_RAW_DIR", "/opt/airflow/data/raw")
DATA_PROCESSED_DIR = os.environ.get("DATA_PROCESSED_DIR", "/opt/airflow/data/processed")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_all_json():

    raw_directory = Path(DATA_RAW_DIR)

    json_files = sorted(
        raw_directory.glob("*.json")
    )

    if not json_files:

        raise FileNotFoundError(
            "No JSON files found."
        )

    files = []

    for json_file in json_files:

        logging.info(
            f"Loading {json_file.name}"
        )

        with open(json_file, "r", encoding="utf-8") as file:

            data = json.load(file)

        files.append(
            (data, json_file)
        )

    return files


def transform_weather_data(data):

    daily_data = data["daily"]

    df = pd.DataFrame({

        "date": daily_data["time"],

        "temperature_max": (
            daily_data["temperature_2m_max"]
        ),

        "temperature_min": (
            daily_data["temperature_2m_min"]
        ),

        "precipitation_mm": (
            daily_data["precipitation_sum"]
        )

    })

    # Convert date to datetime
    df["date"] = pd.to_datetime(
        df["date"]
    )

    # Add location
    metadata = data.get("metadata", {})

    df["location"] = metadata.get("location", "unknown")

    df["latitude"] = metadata.get("latitude")

    df["longitude"] = metadata.get("longitude")

    df["extracted_at"] = (
        pd.to_datetime(metadata.get("extracted_at"), utc=True)
        .round("us")
    )
    
    df["extracted_at"] = df["extracted_at"].dt.tz_localize(None)

    return df


def save_processed_data(df, latest_file):

    processed_directory = Path(
        DATA_PROCESSED_DIR
    )

    processed_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
    processed_directory
    / latest_file.with_suffix(".parquet").name
    )
    
    df["date"] = pd.to_datetime(
        df["date"]
    ).dt.date

    df = df.sort_values("date")

    logging.info(df.dtypes)
    logging.info(df["extracted_at"].head())
    
    df.to_parquet(
        output_file,
        index=False,
        engine="pyarrow",
        coerce_timestamps="us",
        allow_truncated_timestamps=True
    )

    logging.info(
        f"Rows processed: {len(df)}"
    )

    logging.info(
        f"Processed data saved to: {output_file}"
    )


def transform():

    logging.info(
        "Starting data transformation..."
    )

    files = load_all_json()

    processed = []

    for data, json_file in files:

        logging.info(
            f"Transforming {json_file.name}"
        )

        df = transform_weather_data(data)

        save_processed_data(
            df,
            json_file
        )

        processed.append(df)

    logging.info(
        f"Successfully transformed {len(processed)} files."
    )

    return processed


if __name__ == "__main__":

    transform()