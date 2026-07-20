import pandas as pd


def flood_risk_score(
    rainfall_3_day
):

    if rainfall_3_day >= 75:

        return "CRITICAL"

    elif rainfall_3_day >= 40:

        return "WARNING"

    else:

        return "NORMAL"


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
            flood_risk_score
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


def main():

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

    print(
        "Risk calculations completed."
    )

    print(df)


if __name__ == "__main__":

    main()