import json
import logging
from datetime import datetime
from pathlib import Path

import requests


# --------------------------------------------------
# 1. BASIC CONFIGURATION
# --------------------------------------------------

LATITUDE = 6.4531
LONGITUDE = 3.3958

LOCATION_NAME = "lagos"


# --------------------------------------------------
# 2. SET UP LOGGING
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# --------------------------------------------------
# 3. FETCH WEATHER DATA
# --------------------------------------------------

def fetch_weather(lat, lon):
    """
    Fetch weather data from Open-Meteo API.
    """

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,rain"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        "&forecast_days=7"
        "&timezone=Africa%2FLagos"
    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    data = response.json()

    return data


# --------------------------------------------------
# 4. SAVE RAW DATA
# --------------------------------------------------

def save_raw(data, location_name):
    """
    Save raw API response as a timestamped JSON file.
    """

    raw_directory = Path("data/raw")

    raw_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"{location_name}_{timestamp}.json"

    file_path = raw_directory / filename

    with open(file_path, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return file_path


# --------------------------------------------------
# 5. PIPELINE FUNCTION
# --------------------------------------------------

def extract():
    """
    Execute the complete data extraction process.

    This function:
    1. Fetches weather data from the API.
    2. Saves the raw response to data/raw.
    3. Returns the path to the saved file.
    """

    logging.info(
        "Starting weather data extraction..."
    )

    # Fetch data from API
    weather_data = fetch_weather(
        LATITUDE,
        LONGITUDE
    )

    logging.info(
        "Weather data successfully fetched."
    )

    # Save raw data
    file_path = save_raw(
        weather_data,
        LOCATION_NAME
    )

    logging.info(
        f"Raw weather data saved to: {file_path}"
    )

    return file_path


# --------------------------------------------------
# 6. RUN DIRECTLY
# --------------------------------------------------

if __name__ == "__main__":

    try:

        extract()

    except Exception as error:

        logging.exception(
            "Weather extraction failed: %s",
            error
        )

        raise