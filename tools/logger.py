import logging
from os import getenv

DEBUG_LEVEL = logging.INFO if getenv("DEBUG", "false").lower() == "false" else logging.DEBUG

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(DEBUG_LEVEL)