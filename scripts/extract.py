import json
import logging
from datetime import datetime
from pathlib import Path
import requests
import os

DATA_RAW_DIR = os.environ.get("DATA_RAW_DIR", "/opt/airflow/data/raw")

# --------------------------------------------------
# NEW: LOCATION CONFIGURATION
# Reads ALL locations from config/locations.json
# --------------------------------------------------

CONFIG_DIR = Path("config")
LOCATIONS_FILE = CONFIG_DIR / "locations.json"

# --------------------------------------------------
# LOGGING
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# NEW: LOAD LOCATIONS
# --------------------------------------------------

def load_locations():
    """
    Load all locations from config/locations.json
    """

    if not LOCATIONS_FILE.exists():
        raise FileNotFoundError(
            f"{LOCATIONS_FILE} not found."
        )

    with open(LOCATIONS_FILE, "r") as file:
        return json.load(file)


# --------------------------------------------------
# FETCH WEATHER DATA
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

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


# --------------------------------------------------
# MODIFIED: SAVE RAW DATA
# --------------------------------------------------

def save_raw(
    data,
    location_name,
    latitude,
    longitude
):
    """
    Save raw API response.
    """

    raw_directory = Path(DATA_RAW_DIR)

    raw_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{location_name.lower()}_{timestamp}.json"
    )

    file_path = raw_directory / filename

    data["metadata"] = {

        "location": location_name,

        "latitude": latitude,

        "longitude": longitude,

        "extracted_at": datetime.utcnow().isoformat()

    }

    with open(file_path, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return file_path


# --------------------------------------------------
# MODIFIED: PIPELINE
# --------------------------------------------------

def extract():
    """
    Extract weather data for every location.
    """

    logging.info(
        "Starting weather data extraction..."
    )

    locations = load_locations()

    saved_files = []

    for city in locations:

        location_name = city["name"]

        latitude = city["latitude"]

        longitude = city["longitude"]

        logging.info(
            f"Fetching weather for {location_name}..."
        )

        weather_data = fetch_weather(
            latitude,
            longitude
        )

        file_path = save_raw(
            weather_data,
            location_name,
            latitude,
            longitude
        )

        logging.info(
            f"Saved: {file_path.name}"
        )

        saved_files.append(file_path)

    logging.info(
        f"Successfully extracted data for {len(saved_files)} locations."
    )

    return saved_files


# --------------------------------------------------
# RUN
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