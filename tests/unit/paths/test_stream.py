from typing import Optional

import pytest

from rabbitmq_management._paths import BasePath, Paths


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.STREAM_CONNECTIONS),
        ("test\\vhost", f"{BasePath.STREAM_CONNECTIONS}/test%5Cvhost"),
    ],
)
def test_connections_endpoints(vhost: Optional[str], expected: str):
    assert Paths.stream.connections(vhost=vhost) == expected


def test_connections_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.stream.connections(vhost="")


def test_connection_details_endpoint():
    assert (
        Paths.stream.connection_details("test\\vhost", "test\\connection")
        == f"{BasePath.STREAM_CONNECTIONS}/test%5Cvhost/test%5Cconnection"
    )


@pytest.mark.parametrize(
    "vhost, connection",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_connection_details_should_raise_error_when_name_is_empty(
    vhost: str, connection: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.stream.connection_details(vhost, connection)


def test_connection_publishers_endpoint():
    assert (
        Paths.stream.connection_publishers("test\\vhost", "test\\connection")
        == f"{BasePath.STREAM_CONNECTIONS}/test%5Cvhost/test%5Cconnection/publishers"
    )


@pytest.mark.parametrize(
    "vhost, connection",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_connection_publishers_should_raise_error_when_name_is_empty(
    vhost: str, connection: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.stream.connection_publishers(vhost, connection)


def test_connection_consumers_endpoint():
    assert (
        Paths.stream.connection_consumers("test\\vhost", "test\\connection")
        == f"{BasePath.STREAM_CONNECTIONS}/test%5Cvhost/test%5Cconnection/consumers"
    )


@pytest.mark.parametrize(
    "vhost, connection",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_connection_consumers_should_raise_error_when_name_is_empty(
    vhost: str, connection: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.stream.connection_consumers(vhost, connection)


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.STREAM_PUBLISHERS),
        ("test\\vhost", f"{BasePath.STREAM_PUBLISHERS}/test%5Cvhost"),
    ],
)
def test_publishers_endpoints(vhost: Optional[str], expected: str):
    assert Paths.stream.publishers(vhost=vhost) == expected


def test_publishers_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.stream.publishers(vhost="")


def test_stream_publishers_endpoint():
    assert (
        Paths.stream.stream_publishers("test\\vhost", "test\\stream")
        == f"{BasePath.STREAM_PUBLISHERS}/test%5Cvhost/test%5Cstream"
    )


@pytest.mark.parametrize(
    "vhost, stream",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_stream_publishers_should_raise_error_when_name_is_empty(
    vhost: str, stream: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.stream.stream_publishers(vhost, stream)


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.STREAM_CONSUMERS),
        ("test\\vhost", f"{BasePath.STREAM_CONSUMERS}/test%5Cvhost"),
    ],
)
def test_consumers_endpoints(vhost: Optional[str], expected: str):
    assert Paths.stream.consumers(vhost=vhost) == expected


def test_consumers_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.stream.consumers(vhost="")
