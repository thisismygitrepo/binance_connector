import responses
from binance_connector.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/bswap/pools", mock_item, 200)
def test_bswap_pools():
    """Tests the API endpoint to list All Swap Pools"""

    client = Client(key, secret)
    response = client.bswap_pools()
    response.should.equal(mock_item)
