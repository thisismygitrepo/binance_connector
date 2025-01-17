import responses

from tests.util import random_str
from tests.util import mock_http_response
from binance_connector.spot import Spot as Client
from binance_connector.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


def test_sub_account_enable_margin_without_email():
    """Tests the API endpoint to enable margin without email"""

    client = Client(key, secret)
    client.sub_account_enable_margin.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.POST,
    "/sapi/v1/sub-account/margin/enable\\?email=alice@test.com",
    mock_item,
    200,
)
def test_sub_account_enable_margin():
    """Tests the API endpoint to enable margin"""

    client = Client(key, secret)
    response = client.sub_account_enable_margin(email="alice@test.com")
    response.should.equal(mock_item)
