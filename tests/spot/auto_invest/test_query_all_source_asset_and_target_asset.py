import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"recvWindow": 5000}
expected_params = {"recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/lending/auto-invest/all/asset\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_query_all_source_asset_and_target_asset():
    """Tests the API endpoint to query all source asset and target asset"""

    client = Client(key, secret)
    response = client.query_all_source_asset_and_target_asset(**send_params)
    response.should.equal(mock_item)
