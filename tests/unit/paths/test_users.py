from typing import Optional

import pytest

from rabbitmq_management.paths import BasePath, UserLimitName, Paths


def test_all_users_endpoint():
    assert Paths.users.all() == BasePath.USERS


def test_user_detail_endpoint():
    assert Paths.users.detail("test\\user") == f"{BasePath.USERS}/test%5Cuser"


def test_users_endoint_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.users.detail(username="")


def test_users_without_permissions_endpoint():
    assert Paths.users.without_permissions() == f"{BasePath.USERS}/without-permissions"


def test_users_bulk_delete_endpoint():
    assert Paths.users.bulk_delete() == f"{BasePath.USERS}/bulk-delete"


def test_user_permissions_endpoint():
    assert (
        Paths.users.permissions("test\\user")
        == f"{BasePath.USERS}/test%5Cuser/permissions"
    )


def test_user_topic_permissions_endpoint():
    assert (
        Paths.users.topic_permissions("test\\user")
        == f"{BasePath.USERS}/test%5Cuser/topic-permissions"
    )


def test_user_permissions_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.users.permissions(username="")


@pytest.mark.parametrize(
    "username, expected",
    [
        (None, BasePath.USER_LIMITS),
        ("test\\user", f"{BasePath.USER_LIMITS}/test%5Cuser"),
    ],
)
def test_user_limits_endpoints(username: Optional[str], expected: str):
    assert Paths.users.limits(username=username) == expected


def test_user_limits_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.users.limits(username="")


@pytest.mark.parametrize(
    "username, limit, expected",
    [
        (
            "test\\username",
            "max-connections",
            f"{BasePath.USER_LIMITS}/test%5Cusername/max-connections",
        ),
        (
            "test\\username",
            "max-channels",
            f"{BasePath.USER_LIMITS}/test%5Cusername/max-channels",
        ),
    ],
)
def test_users_set_limits_endpoints(username: str, limit: UserLimitName, expected: str):
    assert Paths.users.set_limits(username, limit) == expected


def test_users_set_limits_should_raises_error_when_name_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.users.set_limits(username="", limit="max-connections")


@pytest.mark.parametrize(
    "username, limit",
    [
        ("test", ""),
        ("test", "test"),
    ],
)
def test_users_set_limits_should_raises_error_when_limit_is_invalid(
    username: str, limit: UserLimitName
):
    with pytest.raises(ValueError, match="('max-connections', 'max-channels')"):
        Paths.users.set_limits(username, limit)
