""" Constants for the TQ Energy Integration """

import logging
from datetime import timedelta

_LOGGER = logging.getLogger(__package__)

DOMAIN = "tqenergymanagement"
DEFAULT_NAME = "tq_em"
DEFAULT_TIMEOUT = 30
READ_PATH = "/mum-webservice/data.php"
LOGIN_PATH = "/start.php"
BASE_URL = "http://{0}:{1}{2}"
MIN_UPDATE_INTERVAL = timedelta(minutes=1)
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=15)