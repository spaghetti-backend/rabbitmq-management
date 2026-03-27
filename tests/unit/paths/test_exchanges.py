from typing import Optional

import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_exchanges_endpoint():
    assert Paths.exchanges.all() == BasePath.EXCHANGES


def test_exchanges_by_vhost_endpoint():
    assert (
        Paths.exchanges.by_vhost("test\\vhost") == f"{BasePath.EXCHANGES}/test%5Cvhost"
    )


def test_exchanges_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.exchanges.by_vhost(vhost="")


@pytest.mark.parametrize(
    "vhost, exchange, if_unused, expected",
    [
        (
            "test\\vhost",
            "test\\exchange",
            False,
            f"{BasePath.EXCHANGES}/test%5Cvhost/test%5Cexchange",
        ),
        (
            "test\\vhost",
            "test\\exchange",
            True,
            f"{BasePath.EXCHANGES}/test%5Cvhost/test%5Cexchange?if-unused=true",
        ),
    ],
)
def test_exchange_detail_endpoint(
    vhost: str, exchange: str, if_unused: bool, expected: str
):
    assert Paths.exchanges.detail(vhost, exchange, if_unused=if_unused) == expected


@pytest.mark.parametrize(
    "vhost, exchange",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_exchange_detail_should_raise_error_when_name_is_empty(
    vhost: str, exchange: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.exchanges.detail(vhost, exchange)


def test_exchange_source_bindings():
    assert (
        Paths.exchanges.source_bindings("test\\vhost", "test\\exchange")
        == f"{BasePath.EXCHANGES}/test%5Cvhost/test%5Cexchange/bindings/source"
    )


@pytest.mark.parametrize(
    "vhost, exchange",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_exchange_source_bindings_should_raise_error_when_name_is_empty(
    vhost: str, exchange: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.exchanges.source_bindings(vhost, exchange)


def test_exchange_destination_bindings():
    assert (
        Paths.exchanges.destination_bindings("test\\vhost", "test\\exchange")
        == f"{BasePath.EXCHANGES}/test%5Cvhost/test%5Cexchange/bindings/destination"
    )


@pytest.mark.parametrize(
    "vhost, exchange",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_exchange_destination_bindings_should_raise_error_when_name_is_empty(
    vhost: str, exchange: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.exchanges.destination_bindings(vhost, exchange)


def test_publish_to_exchange():
    assert (
        Paths.exchanges.publish("test\\vhost", "test\\exchange")
        == f"{BasePath.EXCHANGES}/test%5Cvhost/test%5Cexchange/publish"
    )


@pytest.mark.parametrize(
    "vhost, exchange",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_publish_to_exchange_raises_error_when_name_is_empty(vhost: str, exchange: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.exchanges.publish(vhost, exchange)
