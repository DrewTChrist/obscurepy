import logging
import sys

format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(format_str)


def get_verbose_logger(module_name):
    """Gets a logger that writes to the console using a StreamHandler

    Args:
        **module_name (str)**: Name of the module requesting the logger

    Returns:
        A logger using a StreamHandler
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_file_logger(module_name):
    """Gets a logger that writes to a file using a FileHandler

    Args:
        **module_name (str)**: Name of the module requesting the logger

    Returns:
        A logger using a FileHandler
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('obscurepy.log')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_null_logger(module_name):
    """Gets a logger with a NullHandler that actually does no logging

    Args:
        **module_name (str)**: Name of the module requesting the logger

    Returns:
        A logger using a NullHandler
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.WARNING)
    handler = logging.NullHandler()
    handler.setLevel(logging.WARNING)
    logger.addHandler(handler)
    return logger
