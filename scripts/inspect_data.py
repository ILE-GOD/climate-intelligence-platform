import pandas as pd

# 1. TRANSFORMED DATA INSPECTION

weather = pd.read_parquet(
    "data/processed/weather.parquet"
)

print("\n========== WEATHER DATA ==========\n")

print(weather)


# 2. FEATURE-ENGINEERED DATA INSPECTION

features = pd.read_parquet(
    "data/processed/weather_features.parquet"
)

print("\n========== FEATURE DATA ==========\n")

print(features)


# 3. FINAL RISK DATA INSPECTION

risk = pd.read_parquet(
    "data/processed/weather_risk.parquet"
)

print("\n========== RISK DATA ==========\n")

print(risk)




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
risk_columns = [
    "date",
    "rainfall_3_day_total",
    "rainfall_7_day_total",
    "flood_risk",
    "sustained_flood_risk",
    "soil_saturation_risk",
    "crop_stress",
    "pond_overflow_risk"
]

print(
    df[risk_columns]
)