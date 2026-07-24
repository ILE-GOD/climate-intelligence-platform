import logging
import pandas as pd

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

    input_file = (
        "data/processed/weather.parquet"
    )

    output_file = (
        "data/processed/weather_features.parquet"
    )

    # Load data
    df = pd.read_parquet(
        input_file
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
        f"Feature-engineered data saved to: {output_file}"
    )

    logging.info(
        "Feature engineering completed successfully."
    )

    return df

if __name__ == "__main__":
    feature_engineering()