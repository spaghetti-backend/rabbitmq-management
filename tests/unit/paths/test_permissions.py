import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_permissions_endpoint():
    assert Paths.permissions.all() == BasePath.PERMISSIONS


def test_individual_permissions_endpoint():
    assert (
        Paths.permissions.individual("test\\vhost", "test\\user")
        == f"{BasePath.PERMISSIONS}/test%5Cvhost/test%5Cuser"
    )


@pytest.mark.parametrize(
    "vhost, username",
    [
        ("", "username"),
        ("vhost", ""),
    ],
)
def test_individual_permissions_raises_error_when_name_is_empty(
    vhost: str, username: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.permissions.individual(vhost=vhost, username=username)


def test_all_topic_permissions_endpoint():
    assert Paths.permissions.topic.all() == BasePath.TOPIC_PERMISSIONS


def test_individual_topic_permissions_endpoints():
    assert (
        Paths.permissions.topic.individual("test\\vhost", "test\\user")
        == f"{BasePath.TOPIC_PERMISSIONS}/test%5Cvhost/test%5Cuser"
    )


@pytest.mark.parametrize(
    "vhost, username",
    [
        ("", "username"),
        ("vhost", ""),
    ],
)
def test_individual_topic_permissions_raises_error_when_name_is_empty(
    vhost: str, username: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.permissions.topic.individual(vhost=vhost, username=username)
