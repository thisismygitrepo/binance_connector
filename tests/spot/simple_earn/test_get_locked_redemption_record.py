import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"current": 1, "size": 100, "recvWindow": 5000}
expected_params = {"current": 1, "size": 100, "recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/simple-earn/locked/history/redemptionRecord\\?"
    + urlencode(expected_params),
    mock_item,
    200,
)
def test_get_locked_redemption_record():
    """Tests the API endpoint to get locked redemption record"""

    client = Client(key, secret)
    response = client.get_locked_redemption_record(**send_params)
    response.should.equal(mock_item)
