from typing import Optional

import pytest

from rabbitmq_management.paths import BasePath, Paths, VHostLimitName


def test_all_vhosts_endpoint():
    assert Paths.vhosts.all() == BasePath.VHOSTS


def test_vhost_detail_endpoint():
    assert Paths.vhosts.detail("test\\vhost") == f"{BasePath.VHOSTS}/test%5Cvhost"


def test_vhosts_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.detail(vhost="")


def test_vhost_connections_endpoint():
    assert (
        Paths.vhosts.connections("test\\vhost")
        == f"{BasePath.VHOSTS}/test%5Cvhost/connections"
    )


def test_vhost_connections_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.connections(vhost="")


def test_vhost_channels_endpoint():
    assert (
        Paths.vhosts.channels("test\\vhost")
        == f"{BasePath.VHOSTS}/test%5Cvhost/channels"
    )


def test_vhost_channels_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.channels(vhost="")


def test_vhost_permissions_endpoint():
    assert (
        Paths.vhosts.permissions("test\\vhost")
        == f"{BasePath.VHOSTS}/test%5Cvhost/permissions"
    )


def test_vhost_permissions_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.permissions(vhost="")


def test_vhost_topic_permissions_endpoint():
    assert (
        Paths.vhosts.topic_permissions("test\\vhost")
        == f"{BasePath.VHOSTS}/test%5Cvhost/topic-permissions"
    )


def test_vhost_topic_permissions_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.topic_permissions(vhost="")


def test_vhost_start_node_endpoint():
    assert (
        Paths.vhosts.start("test\\vhost", "test\\node")
        == f"{BasePath.VHOSTS}/test%5Cvhost/start/test%5Cnode"
    )


@pytest.mark.parametrize(
    "vhost, node",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_vhost_start_node_should_raises_error_when_name_is_empty(vhost: str, node: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.start(vhost, node)


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.VHOST_LIMITS),
        ("test\\vhost", f"{BasePath.VHOST_LIMITS}/test%5Cvhost"),
    ],
)
def test_vhost_limits_endpoints(vhost: Optional[str], expected: str):
    assert Paths.vhosts.limits(vhost=vhost) == expected


def test_vhost_limits_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.limits(vhost="")


@pytest.mark.parametrize(
    "vhost, limit, expected",
    [
        (
            "test\\vhost",
            "max-connections",
            f"{BasePath.VHOST_LIMITS}/test%5Cvhost/max-connections",
        ),
        (
            "test\\vhost",
            "max-queues",
            f"{BasePath.VHOST_LIMITS}/test%5Cvhost/max-queues",
        ),
    ],
)
def test_vhost_set_limits_endpoints(vhost: str, limit: VHostLimitName, expected: str):
    assert Paths.vhosts.set_limits(vhost, limit) == expected


def test_vhost_set_limits_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.vhosts.set_limits(vhost="", limit="max-connections")


@pytest.mark.parametrize(
    "vhost, limit",
    [
        ("test", ""),
        ("test", "test"),
    ],
)
def test_vhost_set_limits_should_raises_error_when_limit_is_invalid(
    vhost: str, limit: VHostLimitName
):
    with pytest.raises(ValueError, match=r"('max-connections', 'max-queues')"):
        Paths.vhosts.set_limits(vhost, limit)
