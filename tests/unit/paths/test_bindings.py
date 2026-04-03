from typing import Optional

import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_bindings_endpoint():
    assert Paths.bindings.all() == BasePath.BINDINGS


def test_vhost_bindings_endpoint():
    assert Paths.bindings.by_vhost("test\\vhost") == f"{BasePath.BINDINGS}/test%5Cvhost"


def test_vhost_bindings_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.bindings.by_vhost(vhost="")


@pytest.mark.parametrize(
    "vhost, exchange, queue, props, expected",
    [
        (
            "test\\vhost",
            "test\\exchange",
            "test\\queue",
            None,
            f"{BasePath.BINDINGS}/test%5Cvhost/e/test%5Cexchange/q/test%5Cqueue",
        ),
        (
            "test\\vhost",
            "test\\exchange",
            "test\\queue",
            "test\\props",
            f"{BasePath.BINDINGS}/test%5Cvhost/e/test%5Cexchange/q/test%5Cqueue/test%5Cprops",
        ),
    ],
)
def test_binding_exchange_to_queue_endpoints(
    vhost: str, exchange: str, queue: str, props: Optional[str], expected: str
):
    assert (
        Paths.bindings.exchange_to_queue(vhost, exchange, queue, props=props)
        == expected
    )


@pytest.mark.parametrize(
    "vhost, exchange, queue, props",
    [
        ("", "exchange", "queue", "props"),
        ("vhost", "exchange", "", "props"),
        ("vhost", "exchange", "queue", ""),
    ],
)
def test_binding_exchange_to_queue_raises_error_when_name_is_empty(
    vhost: str, exchange: str, queue: str, props: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.bindings.exchange_to_queue(vhost, exchange, queue, props=props)


@pytest.mark.parametrize(
    "vhost, source, destination, props, expected",
    [
        (
            "test\\vhost",
            "test\\source",
            "test\\destination",
            None,
            f"{BasePath.BINDINGS}/test%5Cvhost/e/test%5Csource/e/test%5Cdestination",
        ),
        (
            "test\\vhost",
            "test\\source",
            "test\\destination",
            "test\\props",
            f"{BasePath.BINDINGS}/test%5Cvhost/e/test%5Csource/e/test%5Cdestination/test%5Cprops",
        ),
    ],
)
def test_binding_exchange_to_exchange_endpoints(
    vhost: str, source: str, destination: str, props: Optional[str], expected: str
):
    assert (
        Paths.bindings.exchange_to_exchange(vhost, source, destination, props=props)
        == expected
    )


@pytest.mark.parametrize(
    "vhost, source, destination, props",
    [
        ("", "source", "destination", "props"),
        ("vhost", "source", "destination", ""),
    ],
)
def test_binding_exchange_to_exchange_raises_error_when_name_is_empty(
    vhost: str, source: str, destination: str, props: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.bindings.exchange_to_exchange(vhost, source, destination, props=props)
