import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_attempts_endpoint():
    assert Paths.auth.attempts("test\\node") == f"{BasePath.AUTH_ATTEMPTS}/test%5Cnode"


def test_attempts_should_raise_error_when_invalid_node_provided():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.auth.attempts(node="")


def test_attempts_by_source_endpoint():
    assert (
        Paths.auth.attempts_by_source("test\\node", "192.168.0.1")
        == f"{BasePath.AUTH_ATTEMPTS}/test%5Cnode/192.168.0.1"
    )


@pytest.mark.parametrize(
    "node, source",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_attempts_by_source_should_raise_error_when_invalid_node_provided(
    node: str, source: str
):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.auth.attempts_by_source(node, source)


def test_hash_password_endpoint():
    assert (
        Paths.auth.hash_password("test\\password")
        == f"{BasePath.AUTH_HASH_PASSWORD}/test%5Cpassword"
    )


def test_hash_password_should_raise_error_when_password_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.auth.hash_password(password="")
