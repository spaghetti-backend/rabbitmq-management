import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_definitions_endpoint():
    assert Paths.definitions.all() == BasePath.DEFINITIONS


def test_definitions_by_vhost_endpoint():
    assert (
        Paths.definitions.by_vhost("test\\vhost")
        == f"{BasePath.DEFINITIONS}/test%5Cvhost"
    )


def test_definitions_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.definitions.by_vhost(vhost="")
