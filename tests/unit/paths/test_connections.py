import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_connections_endpoint():
    assert Paths.connections.all() == BasePath.CONNECTIONS


def test_connection_detail_endpoint():
    assert (
        Paths.connections.detail("test\\connection")
        == f"{BasePath.CONNECTIONS}/test%5Cconnection"
    )


def test_connection_detail_should_raise_error_when_connection_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.connections.detail(connection="")


def test_connections_by_user_endpoint():
    assert (
        Paths.connections.by_user("test\\user")
        == f"{BasePath.CONNECTIONS}/username/test%5Cuser"
    )


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
