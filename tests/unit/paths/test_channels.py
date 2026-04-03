import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_channels_endpoint():
    assert Paths.channels.all() == BasePath.CHANNELS


def test_channel_detail_endpoint():
    assert (
        Paths.channels.detail("test\\channel") == f"{BasePath.CHANNELS}/test%5Cchannel"
    )


def test_channel_detail_should_raise_error_when_channel_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.channels.detail(channel="")
