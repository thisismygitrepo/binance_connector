#!/usr/bin/env python

import logging
from binance_connector.spot import Spot as Client
from binance_connector.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

# historical_trades requires api key in request header
spot_client = Client(base_url="https://testnet.binance.vision")

logging.info(spot_client.historical_trades("BTCUSDT"))
logging.info(spot_client.historical_trades("BTCUSDT", limit=10, fromId="100"))
