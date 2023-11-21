#!/usr/bin/env python

import logging
from binance_connector.spot import Spot as Client
from binance_connector.lib.utils import config_logging
from binance_connector.error import ClientError

from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

api_key, api_secret = get_api_key()

client = Client(api_key, api_secret)

try:
    response = client.query_sub_account_assets("alice@test.com", recvWindow=5000)
    logger.info(response)
except ClientError as error:
    logger.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
