import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "product": "STAKING",
    "txnType": "SUBSCRIPTION",
    "recvWindow": 5000,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/staking/stakingRecord\\?" + urlencode(params),
    mock_item,
    200,
)
def test_staking_history():
    """Tests the API endpoint to staking history"""

    client = Client(key, secret)
    response = client.staking_history(**params)
    response.should.equal(mock_item)
