import logging
import os
from datetime import datetime

def get_logger(name):
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(f"logs/{datetime.now().date()}.log")
        formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(logging.StreamHandler())
    return logger
