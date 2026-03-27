from typing import Optional

import pytest

from rabbitmq_management._paths import BasePath, Paths


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.POLICIES),
        ("test\\policy", f"{BasePath.POLICIES}/test%5Cpolicy"),
    ],
)
def test_policies_endpoints(vhost: Optional[str], expected: str):
    assert Paths.policies(vhost=vhost) == expected


def test_policies_should_raise_error_when_policy_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.policies(vhost="")


def test_policy_detail_endpoint():
    assert (
        Paths.policies.detail("test\\vhost", "test\\policy")
        == f"{BasePath.POLICIES}/test%5Cvhost/test%5Cpolicy"
    )


@pytest.mark.parametrize(
    "vhost, policy",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_policy_detail_should_raise_error_when_name_is_empty(vhost: str, policy: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.policies.detail(vhost, policy)


@pytest.mark.parametrize(
    "vhost, expected",
    [
        (None, BasePath.OPERATOR_POLICIES),
        ("test\\policy", f"{BasePath.OPERATOR_POLICIES}/test%5Cpolicy"),
    ],
)
def test_operator_policies_endpoints(vhost: Optional[str], expected: str):
    assert Paths.operator_policies(vhost=vhost) == expected


def test_operator_policies_should_raise_error_when_policy_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.operator_policies(vhost="")


def test_operator_policy_detail_endpoint():
    assert (
        Paths.operator_policies.detail("test\\vhost", "test\\policy")
        == f"{BasePath.OPERATOR_POLICIES}/test%5Cvhost/test%5Cpolicy"
    )


@pytest.mark.parametrize(
    "vhost, policy",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_operator_policy_detail_should_raise_error_when_name_is_empty(
    vhost: str, policy: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.operator_policies.detail(vhost, policy)
