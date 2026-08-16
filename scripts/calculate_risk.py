import logging
import os
from pathlib import Path

import pandas as pd


DATA_PROCESSED_DIR = os.environ.get("DATA_PROCESSED_DIR", "/opt/airflow/data/processed")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def flash_flood_risk(
    rainfall_3_day
):

    if rainfall_3_day >= 75:

        return "CRITICAL"

    elif rainfall_3_day >= 40:

        return "WARNING"

    else:

        return "NORMAL"

def sustained_flood_risk(
    rainfall_7_day
):

    if rainfall_7_day >= 100:

        return "CRITICAL"

    elif rainfall_7_day >= 60:

        return "WARNING"

    else:

        return "NORMAL"

def soil_saturation_risk(
    rainfall_7_day
):

    if rainfall_7_day >= 100:

        return "HIGH"

    elif rainfall_7_day >= 60:

        return "MEDIUM"

    else:

        return "LOW"

def crop_stress_index(
    temperature
):

    if temperature >= 35:

        return "HIGH"

    elif temperature >= 30:

        return "MEDIUM"

    else:

        return "LOW"


def pond_overflow_risk(
    rainfall_3_day
):

    if rainfall_3_day >= 75:

        return "HIGH"

    elif rainfall_3_day >= 40:

        return "MEDIUM"

    else:

        return "LOW"

def calculate_risks(df):

    df["flood_risk"] = (
        df["rainfall_3_day_total"]
        .apply(
            flash_flood_risk
        )
    )

    df["sustained_flood_risk"] = (
        df["rainfall_7_day_total"]
        .apply(
            sustained_flood_risk
        )
    )

    df["soil_saturation_risk"] = (
        df["rainfall_7_day_total"]
        .apply(
            soil_saturation_risk
        )
    )

    df["crop_stress"] = (
        df["temperature_max"]
        .apply(
            crop_stress_index
        )
    )

    df["pond_overflow_risk"] = (
        df["rainfall_3_day_total"]
        .apply(
            pond_overflow_risk
        )
    )

    return df

def calculate_risk():

    logging.info(
        "Starting risk calculations..."
    )

    processed_directory = Path(DATA_PROCESSED_DIR)

    feature_files = sorted(
        processed_directory.glob(
            "*_features.parquet"
        )
    )

    if not feature_files:

        raise FileNotFoundError(
            "No feature-engineered parquet files found."
        )

    processed_count = 0

    for input_file in feature_files:

        logging.info(
            f"Processing: {input_file.name}"
        )

        output_file = (
            processed_directory
            / input_file.name.replace(
                "_features.parquet",
                "_risk.parquet"
            )
        )

        # Load features
        df = pd.read_parquet(
            input_file
        )

        # Calculate risks
        df = calculate_risks(
            df
        )

        # Save output
        df.to_parquet(
            output_file,
            index=False
        )

        logging.info(
            f"Rows processed: {len(df)}"
        )

        logging.info(
            f"Saved: {output_file.name}"
        )

        processed_count += 1

    logging.info(
        f"Risk calculations completed for {processed_count} files."
    )


if __name__ == "__main__":

    calculate_risk()
