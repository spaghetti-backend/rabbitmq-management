from typing import Optional

import pytest

from rabbitmq_management._paths import BasePath, Paths


@pytest.mark.parametrize(
    "connection, expected",
    [
        (None, BasePath.CONNECTIONS),
        ("test\\connection", f"{BasePath.CONNECTIONS}/test%5Cconnection"),
    ],
)
def test_connections_endpoints(connection: Optional[str], expected: str):
    assert Paths.connections(connection=connection) == expected


def test_connections_should_raise_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.connections(connection="")


def test_connections_by_user_should_raise_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.connections.by_user(username="")


def test_connection_channels_endpoint():
    assert (
        Paths.connections.channels("test\\connection")
        == f"{BasePath.CONNECTIONS}/test%5Cconnection/channels"
    )


def test_connection_channels_should_raise_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.connections.channels(connection="")
