import responses
from binance_connector.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/sapi/v1/blvt/userLimit", mock_item, 200)
def test_user_limit_info():
    """Tests the API endpoint to get user's limit info"""

    client = Client(key, secret)
    response = client.user_limit_info()
    response.should.equal(mock_item)
