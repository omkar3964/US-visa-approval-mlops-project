# logger_module.py

import os
import logging
from datetime import datetime
def get_logger(log_name: str = "app"):
    """
    Creates and returns a configured logger instance.
    Each run generates a new log file inside 'logs/' folder.

    Args:
        log_name (str): Name of the logger (e.g., 'data_loader', 'mongo_upload')
    """

    # Create logs directory if not exist
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Create unique log filename
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_filename = f"{log_name}_{timestamp}.log"
    log_filepath = os.path.join(log_dir, log_filename)

    # Create and configure logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if logger is reused
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(log_filepath)
        # Console handler
        console_handler = logging.StreamHandler()

        # Formatter
        formatter = logging.Formatter(
            "[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    logger.info(f"Logger initialized: {log_filepath}")
    return logger
