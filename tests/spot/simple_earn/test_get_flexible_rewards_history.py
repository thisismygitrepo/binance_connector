import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"type": "REWARDS"}
expected_params = {"type": "REWARDS"}


@mock_http_response(
    responses.GET,
    "/sapi/v1/simple-earn/flexible/history/rewardsRecord",
    mock_item,
    200,
)
def test_get_flexible_rewards_history():
    """Tests the API endpoint to get flexible rewards history"""

    client = Client(key, secret)
    response = client.get_flexible_rewards_history("REWARDS")
    response.should.equal(mock_item)
