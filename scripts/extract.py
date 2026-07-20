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

    # Raise an error if the API request failed
    response.raise_for_status()

    # Convert the response to Python dictionary
    data = response.json()

    return data


# --------------------------------------------------
# 4. SAVE RAW DATA
# --------------------------------------------------

def save_raw(data, location_name):
    """
    Save raw API response as a timestamped JSON file.
    """

    # Create data/raw directory if it does not exist
    raw_directory = Path("data/raw")
    raw_directory.mkdir(parents=True, exist_ok=True)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create filename
    filename = f"{location_name}_{timestamp}.json"

    # Create complete file path
    file_path = raw_directory / filename

    # Save JSON data
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    return file_path


# --------------------------------------------------
# 5. MAIN FUNCTION
# --------------------------------------------------

def main():

    try:

        logging.info("Starting weather data extraction...")

        # Extract data
        weather_data = fetch_weather(
            LATITUDE,
            LONGITUDE
        )

        logging.info("Weather data successfully fetched.")

        # Save raw data
        file_path = save_raw(
            weather_data,
            LOCATION_NAME
        )

        logging.info(
            f"Raw weather data saved to: {file_path}"
        )

    except Exception as error:

        logging.error(
            f"Weather extraction failed: {error}"
        )


# --------------------------------------------------
# 6. RUN THE PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()