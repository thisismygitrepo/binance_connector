

from binance_connector.websocket.spot.websocket_stream import SpotWebsocketStreamClient

def message_handler(_, message):
    print(message)


my_client = SpotWebsocketStreamClient(on_message=message_handler)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
# my_client.stop()
