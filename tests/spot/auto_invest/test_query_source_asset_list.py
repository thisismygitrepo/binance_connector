import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"usageType": "RECURRING", "recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v1/lending/auto-invest/source-asset/list\\?" + urlencode(send_params),
    mock_item,
    200,
)
def test_query_source_asset_list():
    """Tests the API endpoint to query source asset list"""

    client = Client(key, secret)
    response = client.query_source_asset_list(**send_params)
    response.should.equal(mock_item)
