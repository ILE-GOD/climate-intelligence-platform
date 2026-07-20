import pandas as pd


# Load the final Parquet file
df = pd.read_parquet(
    "data/processed/weather_risk.parquet"
)


# Display the first five rows
print("First five rows:")
print(df.head())


# Display statistical summary
print("\nStatistical summary:")
print(df.describe())


# Display the most important risk columns
print("\nRisk summary:")
print(
    df[
        [
            "date",
            "rainfall_3_day_total",
            "flood_risk",
            "crop_stress",
            "pond_overflow_risk"
        ]
    ]
)