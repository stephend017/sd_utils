import pytest
from examples.api.coinbase import Coinbase
from sd_utils.api.request import GET
from sd_utils.api.client import client_api


@client_api("https://swapi.dev/api")
class SWAPI:
    people = GET("/people")

    # throws the default error
    fake = GET("/fake")


def test_api_request_with_query():
    # if this fails then an exception is raised
    _ = Coinbase.spot_price("BTC-USD/spot")


def test_api_request_without_query():
    # if this fails then an exception is raised
    _ = Coinbase.time()


def test_api_request_fails():
    # this request fails, so it raises an exception
    with pytest.raises(Exception):
        _ = Coinbase.user()


def test_different_api_request():
    # if this fails then an exception is raised
    _ = SWAPI.people("1/")


def test_requests():
    requests = Coinbase.requests()
    assert len(requests) == 3


def test_errors():
    errors = Coinbase.errors()
    assert len(errors) == 2
