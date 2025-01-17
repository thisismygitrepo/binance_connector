#!/usr/bin/env python

import logging
from binance_connector.spot import Spot as Client
from binance_connector.lib.utils import config_logging
from binance_connector.error import ClientError


config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)


client = Client()

try:
    response = client.list_all_convert_pairs(fromAsset="BTC", toAsset="USDT")
    logger.info(response)
except ClientError as error:
    logger.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
