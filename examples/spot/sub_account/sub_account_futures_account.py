#!/usr/bin/env python

import logging
from binance_connector.spot import Spot as Client
from binance_connector.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key()

spot_client = Client(api_key, api_secret)
logging.info(
    spot_client.sub_account_futures_account(
        email="alice@test.com",
        futuresType=1,  # 1:USDT Margined Futures, 2:COIN Margined Futures
    )
)
