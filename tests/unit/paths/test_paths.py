from typing import Optional

import pytest

from rabbitmq_management.paths import Paths, BasePath


def test_aliveness():
    assert (
        Paths.aliveness_test("test\\vhost") == f"{BasePath.ALIVENESS_TEST}/test%5Cvhost"
    )


def test_aliveness_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.aliveness_test(vhost="")


@pytest.mark.parametrize(
    "channel, expected",
    [
        (None, BasePath.CHANNELS),
        ("test@testmq", f"{BasePath.CHANNELS}/test%40testmq"),
    ],
)
def test_channels_endpoints(channel: Optional[str], expected: str):
    assert Paths.channels(channel=channel) == expected


def test_channels_should_raise_error_when_channel_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.channels(channel="")


@pytest.mark.parametrize(
    "consumer, expected",
    [
        (None, BasePath.CONSUMERS),
        ("test@vhost", f"{BasePath.CONSUMERS}/test%40vhost"),
    ],
)
def test_consumers_endpoints(consumer: Optional[str], expected: str):
    assert Paths.consumers(consumer=consumer) == expected


def test_consumers_should_raise_error_when_consumer_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.consumers(consumer="")


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.DEFINITIONS),
        ("test\\vhost", f"{BasePath.DEFINITIONS}/test%5Cvhost"),
    ],
)
def test_definitions_endpoints(vhost: Optional[str], expected: str):
    assert Paths.definitions(vhost=vhost) == expected


def test_definitions_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.definitions(vhost="")


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.FEDERATION_LINKS),
        ("test\\vhost", f"{BasePath.FEDERATION_LINKS}/test%5Cvhost"),
    ],
)
def test_federation_links_endpoints(vhost: Optional[str], expected: str):
    assert Paths.federation_links(vhost=vhost) == expected


def test_federation_links_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.federation_links(vhost="")


@pytest.mark.parametrize(
    "node, memory, binary, expected",
    [
        (None, True, True, BasePath.NODES),
        ("test@testmq", False, False, f"{BasePath.NODES}/test%40testmq"),
        ("test@testmq", True, False, f"{BasePath.NODES}/test%40testmq?memory=true"),
        ("test@testmq", False, True, f"{BasePath.NODES}/test%40testmq?binary=true"),
        (
            "test@testmq",
            True,
            True,
            f"{BasePath.NODES}/test%40testmq?memory=true&binary=true",
        ),
    ],
)
def test_nodes_endpoints(
    node: Optional[str], memory: bool, binary: bool, expected: str
):
    assert Paths.nodes(node=node, memory=memory, binary=binary) == expected


def test_nodes_should_raise_error_when_node_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.nodes(node="")


@pytest.mark.parametrize(
    "vhost, username, expected",
    [
        (None, None, BasePath.PERMISSIONS),
        (
            "test\\vhost",
            "test\\username",
            f"{BasePath.PERMISSIONS}/test%5Cvhost/test%5Cusername",
        ),
    ],
)
def test_permissions_endpoints(
    vhost: Optional[str], username: Optional[str], expected: str
):
    assert Paths.permissions(vhost=vhost, username=username) == expected


@pytest.mark.parametrize(
    "vhost, username",
    [
        ("", "username"),
        ("vhost", ""),
    ],
)
def test_permissions_raises_error_when_name_is_empty(vhost: str, username: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.permissions(vhost=vhost, username=username)


@pytest.mark.parametrize(
    "vhost, username",
    [
        (None, "username"),
        ("vhost", None),
    ],
)
def test_permissions_raises_error_when_both_names_is_not_provided(
    vhost: str, username: str
):
    with pytest.raises(ValueError, match="required"):
        Paths.permissions(vhost=vhost, username=username)


@pytest.mark.parametrize(
    "vhost, username, expected",
    [
        (None, None, BasePath.TOPIC_PERMISSIONS),
        (
            "test\\vhost",
            "test\\username",
            f"{BasePath.TOPIC_PERMISSIONS}/test%5Cvhost/test%5Cusername",
        ),
    ],
)
def test_topic_permissions_endpoints(
    vhost: Optional[str], username: Optional[str], expected: str
):
    assert Paths.topic_permissions(vhost=vhost, username=username) == expected


@pytest.mark.parametrize(
    "vhost, username",
    [
        ("", "username"),
        ("vhost", ""),
    ],
)
def test_topic_permissions_raises_error_when_name_is_empty(vhost: str, username: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.topic_permissions(vhost=vhost, username=username)


@pytest.mark.parametrize(
    "vhost, username",
    [
        (None, "username"),
        ("vhost", None),
    ],
)
def test_topic_permissions_raises_error_when_both_names_is_not_provided(
    vhost: str, username: str
):
    with pytest.raises(ValueError, match="required"):
        Paths.topic_permissions(vhost=vhost, username=username)
