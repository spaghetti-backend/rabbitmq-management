import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_channels_endpoint():
    assert Paths.channels.all() == BasePath.CHANNELS


def test_channels_by_vhost_endpoint():
    assert Paths.channels.by_vhost("test\\vhost") == f"{BasePath.CHANNELS}/test%5Cvhost"


def test_channels_by_vhost_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.channels.by_vhost(vhost="")
