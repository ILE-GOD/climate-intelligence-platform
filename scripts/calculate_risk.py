import logging
import pandas as pd

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

    input_file = (
        "data/processed/"
        "weather_features.parquet"
    )

    output_file = (
        "data/processed/"
        "weather_risk.parquet"
    )

    # Load features
    df = pd.read_parquet(
        input_file
    )

    # Calculate risk indicators
    df = calculate_risks(
        df
    )

    # Save final dataset
    df.to_parquet(
        output_file,
        index=False
    )

    logging.info(
        f"Risk data saved to: {output_file}"
    )

    logging.info(
        "Risk calculations completed successfully."
    )

    return df


if __name__ == "__main__":

    calculate_risk()
