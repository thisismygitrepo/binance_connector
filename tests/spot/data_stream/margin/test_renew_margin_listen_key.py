import responses

from binance_connector.spot import Spot as Client
from tests.util import random_str
from tests.util import mock_http_response
from binance_connector.error import ParameterRequiredError, ClientError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()

listen_key = random_str()


def test_new_listen_key_without_key():
    """Tests the API endpoint to renew margin listenkey but without the key"""

    client = Client(key)
    client.renew_margin_listen_key.when.called_with("").should.throw(
        ParameterRequiredError
    )


@mock_http_response(
    responses.PUT,
    "/sapi/v1/userDataStream\\?listenKey=" + listen_key,
    mock_exception,
    400,
)
def test_rewnew_listen_key_with_wrong_key():
    """Tests the API endpoint to renew margin listekn key with wrong key"""

    client = Client(key)
    client.renew_margin_listen_key.when.called_with(listen_key).should.throw(
        ClientError
    )


@mock_http_response(
    responses.PUT, "/sapi/v1/userDataStream\\?listenKey=" + listen_key, mock_item, 200
)
def test_rewnew_listen_key():
    """Tests the API endpoint to renew an existing margin listen key"""

    client = Client(key)
    response = client.renew_margin_listen_key(listen_key)
    response.should.equal(mock_item)
