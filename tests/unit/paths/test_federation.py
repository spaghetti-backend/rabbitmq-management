import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_federation_links_endpoint():
    assert Paths.federation.links() == BasePath.FEDERATION_LINKS


def test_federation_links_by_vhost_endpoint():
    assert (
        Paths.federation.links_by_vhost("test\\vhost")
        == f"{BasePath.FEDERATION_LINKS}/test%5Cvhost"
    )


def test_federation_links_by_vhost_should_raise_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.federation.links_by_vhost(vhost="")
