import logging
import sys

from scripts.extract import extract
from scripts.validate import validate
from scripts.transform import transform
from scripts.feature_engineering import feature_engineering
from scripts.calculate_risk import calculate_risk


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():

    logging.info(
        "Pipeline started"
    )

    # Step 1: Extract data
    extract()

    logging.info(
        "Extraction completed successfully."
    )

    # Step 2: Validate data
    validate()

    logging.info(
        "Validation completed successfully."
    )

    # Step 3: Transform data
    transform()

    logging.info(
        "Transformation completed successfully."
    )

    # Step 4: Create features
    feature_engineering()

    logging.info(
        "Feature engineering completed successfully."
    )

    # Step 5: Calculate risks
    calculate_risk()

    logging.info(
        "Risk calculation completed successfully."
    )

    logging.info(
        "Pipeline completed successfully."
    )


if __name__ == "__main__":

    try:

        run_pipeline()

    except Exception as error:

        logging.exception(
            "Pipeline failed: %s",
            error
        )

        sys.exit(1)