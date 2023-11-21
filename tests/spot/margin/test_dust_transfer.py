import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"asset": "BTC", "recvWindow": 5000}
expected_params = {"asset": "BTC", "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/margin/dust\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_dust_transfer():
    """Tests the API endpoint to dust transfer"""

    client = Client(key, secret)
    response = client.dust_transfer(**send_params)
    response.should.equal(mock_item)
