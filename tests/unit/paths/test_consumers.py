import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_consumers_endpoint():
    assert Paths.consumers.all() == BasePath.CONSUMERS


def test_consumers_by_vhost_endpoint():
    assert (
        Paths.consumers.by_vhost("test\\vhost") == f"{BasePath.CONSUMERS}/test%5Cvhost"
    )


def test_consumers_by_vhost_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.consumers.by_vhost(vhost="")
