import responses
from binance_connector.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/bswap/liquidityOps", mock_item, 200)
def test_bswap_liquidity():
    """Tests the API endpoint to get liquidity operation (add/remove) records."""

    client = Client(key, secret)
    response = client.bswap_liquidity_operation_record()
    response.should.equal(mock_item)
