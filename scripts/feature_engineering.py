import logging
import os
from pathlib import Path

import pandas as pd

DATA_PROCESSED_DIR = os.environ.get("DATA_PROCESSED_DIR", "/opt/airflow/data/processed")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def add_features(df):

    # Sort by date
    df = df.sort_values(
        "date"
    )

    # 3-day accumulated rainfall
    df["rainfall_3_day_total"] = (
        df["precipitation_mm"]
        .rolling(
            window=3,
            min_periods=1
        )
        .sum()
    )

    # 7-day accumulated rainfall
    df["rainfall_7_day_total"] = (
        df["precipitation_mm"]
        .rolling(
            window=7,
            min_periods=1
        )
        .sum()
    )

    # Daily temperature change
    df["temperature_change"] = (
        df["temperature_max"]
        .diff()
    )

    return df


def feature_engineering():

    logging.info(
        "Starting feature engineering..."
    )

    processed_directory = Path(DATA_PROCESSED_DIR)

    parquet_files = [
        file for file in processed_directory.glob("*.parquet")
        if not file.name.endswith("_features.parquet")
        and not file.name.endswith("_risk.parquet")
    ]

    if not parquet_files:
        raise FileNotFoundError(
            "No processed parquet files found."
        )

    input_file = max(
        parquet_files,
        key=lambda file: file.stat().st_mtime
    )

    output_file = (
        processed_directory
        / input_file.name.replace(
            ".parquet",
            "_features.parquet"
        )
    )

    # Load data
    df = pd.read_parquet(
        input_file
    )
    
    logging.info(
        f"Processing: {input_file.name}"
    )

    # Add features
    df = add_features(
        df
    )

    # Save data
    df.to_parquet(
        output_file,
        index=False
    )
    
    logging.info(
        f"Rows processed: {len(df)}"
    )

    logging.info(
        f"Feature-engineered data saved to: {output_file}"
    )

    logging.info(
        "Feature engineering completed successfully."
    )

    return df

if __name__ == "__main__":
    feature_engineering()