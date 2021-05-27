import logging
import sys

format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(format_str)


def get_verbose_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_file_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('obscurepy.log')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
