import logging
from pythonjsonlogger import jsonlogger
import sys


class RockLogger:
    def __init__(self, name):
        self.name = name

    def get_logger(self):

        # remove all the existing loggers
        root = logging.getLogger()
        if root.hasHandlers():
            for handler in root.handlers:
                root.removeHandler(handler)

        # build our custom json logger, for better log ingestion and parsing
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = jsonlogger.JsonFormatter(
            fmt="%(asctime)s %(levelname)s %(name)s %(lineno)d %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
