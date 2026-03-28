import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_aliveness():
    assert (
        Paths.aliveness_test("test\\vhost") == f"{BasePath.ALIVENESS_TEST}/test%5Cvhost"
    )


def test_aliveness_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.aliveness_test(vhost="")
