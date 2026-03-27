import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_policies_endpoint():
    assert Paths.policies.all() == BasePath.POLICIES


def test_policies_by_vhost_endpoint():
    assert Paths.policies.by_vhost("test\\vhost") == f"{BasePath.POLICIES}/test%5Cvhost"


def test_policies_by_vhost_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.policies.by_vhost(vhost="")


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


def test_all_operator_policies_endpoint():
    assert Paths.operator_policies.all() == BasePath.OPERATOR_POLICIES


def test_operator_policies_by_vhost_endpoint():
    assert (
        Paths.operator_policies.by_vhost("test\\vhost")
        == f"{BasePath.OPERATOR_POLICIES}/test%5Cvhost"
    )


def test_operator_policies_by_vhost_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.operator_policies.by_vhost(vhost="")


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
