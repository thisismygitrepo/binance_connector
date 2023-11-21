import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"autoRepay": True, "recvWindow": 5000}
expected_params = {"autoRepay": True, "recvWindow": 5000}


@mock_http_response(
    responses.POST,
    "/sapi/v1/portfolio/repay-futures-switch\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_change_auto_repay_futures_status():
    """Tests the API endpoint to change auto-repay-futures status"""

    client = Client(key, secret)
    response = client.change_auto_repay_futures_status(**send_params)
    response.should.equal(mock_item)
