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
    "loanCoin": "BUSD",
    "collateralCoin": "BNB",
    "adjustmentAmount": 1.01,
    "direction": "ADDTIONAL",
    "recvWindow": 5000,
}


@mock_http_response(
    responses.POST,
    "/sapi/v1/loan/flexible/adjust/ltv\\?" + urlencode(send_params),
    mock_item,
    200,
)
def test_flexible_loan_adjust_ltv():
    """Tests the API endpoint to adjust ltv - flexible loan adjust ltv"""

    client = Client(key, secret)
    response = client.flexible_loan_adjust_ltv(**send_params)
    response.should.equal(mock_item)
