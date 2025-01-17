import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {
    "sourceType": "MAIN_SITE",
    "subscriptionAmount": 10.1,
    "sourceAsset": "USDT",
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/lending/auto-invest/one-off\\?" + urlencode(send_params),
    mock_item,
    200,
)
def test_one_time_transaction():
    """Tests the API endpoint to one time transaction"""

    client = Client(key, secret)
    response = client.one_time_transaction(**send_params)
    response.should.equal(mock_item)
