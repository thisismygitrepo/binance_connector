import responses
from binance_connector.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, "/api/v3/account", mock_item, 200)
def test_account():
    """Tests the API endpoint to account information"""

    client = Client(key, secret)
    response = client.account()
    response.should.equal(mock_item)


@mock_http_response(responses.GET, "/api/v3/account\\?recvWindow=10000", mock_item, 200)
def test_account_with_recvWindow():
    """Tests the API endpoint to account information with recvWindow"""

    client = Client(key, secret)
    response = client.account(recvWindow=10000)
    response.should.equal(mock_item)
