import os
import sys
import logging

LOG_DEBUG_ENV = "TETRIS_ENGINE_DEBUG"
FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

LOG_LEVEL = logging.DEBUG if os.getenv(LOG_DEBUG_ENV) else logging.INFO


def get_console_handler():
    """
    Returns the console handler.
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_logger(logger_name):
    """
    Args:
        logger_name (str): Name for the logger

    Retruns:
        logger: A logger 
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(get_console_handler())
    logger.propagate = False
    return logger
