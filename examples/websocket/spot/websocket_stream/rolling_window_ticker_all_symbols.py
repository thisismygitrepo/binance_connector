#!/usr/bin/env python

import time
import logging
from binance_connector.lib.utils import config_logging
from binance_connector.websocket.spot.websocket_stream import SpotWebsocketStreamClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler)


my_client.rolling_window_ticker_all_symbols(windowSize="1h")

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
