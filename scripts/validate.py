import json
import logging
from pathlib import Path
import os

DATA_RAW_DIR = os.environ.get("DATA_RAW_DIR", "/opt/airflow/data/raw")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Fields we expect from the API
REQUIRED_FIELDS = [
    "current",
    "daily"
]


def load_json(file_path):
    """
    Load a JSON file.
    """

    with open(file_path, "r") as file:
        data = json.load(file)

    return data


def validate_schema(data):
    """
    Check whether required fields exist.
    """

    errors = []

    for field in REQUIRED_FIELDS:

        if field not in data:
            errors.append(
                f"Missing required field: {field}"
            )

    return errors


def validate_current_weather(data):
    """
    Validate current weather values.
    """

    errors = []

    current_weather = data.get("current", {})

    temperature = current_weather.get(
        "temperature_2m"
    )

    rainfall = current_weather.get("rain")

    # Check for missing temperature
    if temperature is None:

        errors.append(
            "Temperature is missing"
        )

    # Check for missing rainfall
    if rainfall is None:

        errors.append(
            "Rainfall is missing"
        )

    # Check temperature range
    if temperature is not None:

        if temperature < -50 or temperature > 60:

            errors.append(
                f"Temperature is unrealistic: {temperature}"
            )

    # Rainfall cannot be negative
    if rainfall is not None:

        if rainfall < 0:

            errors.append(
                f"Rainfall cannot be negative: {rainfall}"
            )

    return errors


def validate_file(file_path):

    report = {
        "file": str(file_path),
        "valid": True,
        "errors": []
    }

    try:

        data = load_json(file_path)

        # Schema validation
        schema_errors = validate_schema(data)

        # Weather value validation
        weather_errors = validate_current_weather(data)

        # Combine errors
        report["errors"].extend(schema_errors)
        report["errors"].extend(weather_errors)

        # Mark invalid if errors exist
        if report["errors"]:

            report["valid"] = False

    except Exception as error:

        report["valid"] = False

        report["errors"].append(
            str(error)
        )

    return report


def validate():

    raw_directory = Path(DATA_RAW_DIR)

    # Get all JSON files
    json_files = sorted(
        raw_directory.glob("*.json")
    )

    if not json_files:

        error_message = (
            "No JSON files found."
        )

        logging.error(error_message)

        raise FileNotFoundError(
            error_message
        )

    reports = []

    for json_file in json_files:

        logging.info(
            f"Validating: {json_file.name}"
        )

        report = validate_file(json_file)

        reports.append(report)

        if report["valid"]:

            logging.info(
                f"{json_file.name} validation successful."
            )

        else:

            logging.error(
                f"{json_file.name} validation failed."
            )

            for error in report["errors"]:

                logging.error(
                    f"- {error}"
                )

            raise ValueError(
                f"Validation failed for {json_file.name}"
            )

    logging.info(
        f"Successfully validated {len(reports)} files."
    )

    return reports


if __name__ == "__main__":
    validate()