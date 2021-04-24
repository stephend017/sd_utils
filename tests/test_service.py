import pytest
import json
from examples.api.crypto import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_service_endpoints_defined():
    urls = []
    app.config["SERVER_NAME"] = "tetsing"

    with app.test_request_context("test"):
        for rule in app.url_map.iter_rules():
            urls.append(str(rule))

    assert "/rsi" in urls
    assert "/rsi/past" in urls


def test_service_endpoints_return_value(client):
    rv = client.get("/rsi?crypto=BTC")
    return_data = json.loads(rv.data.decode())
    assert return_data["status_code"] == 500


def test_service_different_endpoints_return_value(client):
    rv = client.get("/rsi/past")
    return_data = json.loads(rv.data.decode())
    assert return_data["status_code"] == 503
