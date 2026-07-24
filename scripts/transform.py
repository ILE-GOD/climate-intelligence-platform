import json
import logging
from pathlib import Path

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_latest_json():

    raw_directory = Path("data/raw")

    json_files = list(
        raw_directory.glob("*.json")
    )

    if not json_files:

        raise FileNotFoundError(
            "No JSON files found."
        )

    latest_file = max(
        json_files,
        key=lambda file: file.stat().st_mtime
    )

    logging.info(
        f"Loading file: {latest_file}"
    )

    with open(latest_file, "r") as file:

        data = json.load(file)

    return data


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
    df["location"] = "Lagos"

    return df


def save_processed_data(df):

    processed_directory = Path(
        "data/processed"
    )

    processed_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
        processed_directory
        / "weather.parquet"
    )

    df.to_parquet(
        output_file,
        index=False
    )

    logging.info(
        f"Processed data saved to: {output_file}"
    )


def transform():

    logging.info(
        "Starting data transformation..."
    )

    data = load_latest_json()

    df = transform_weather_data(
        data
    )

    save_processed_data(
        df
    )

    logging.info(
        "Data transformation completed successfully."
    )

    return df


if __name__ == "__main__":

    transform()