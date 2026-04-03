import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_all_vhosts(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("vhosts").respond(text='[{"name": "test"}]')

    response = management_api.vhosts.all()

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


def test_get_vhost_detail(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("vhosts/test").respond(text='{"name": "test"}')

    response = management_api.vhosts.detail(vhost="test")

    assert response.get("name") == "test"


def test_set_vhost(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    mock_json = {
        "description": "virtual host description",
        "tags": "accounts,production",
        "tracing": True,
    }
    api_mock.put("vhosts/test").respond(status_code=httpx.codes.NO_CONTENT)

    management_api.vhosts.set(vhost="test", value=mock_json)


def test_delete_vhost(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete("vhosts/test").respond(status_code=httpx.codes.NO_CONTENT)

    management_api.vhosts.delete(vhost="test")


def test_get_vhost_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test/permissions").respond(text='[{"vhost": "test"}]')

    response = management_api.vhosts.permissions(vhost="test")

    assert isinstance(response, list)
    assert response[0].get("vhost") == "test"


def test_get_vhost_topic_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test/topic-permissions").respond(text='[{"vhost": "test"}]')

    response = management_api.vhosts.topic_permissions(vhost="test")

    assert isinstance(response, list)
    assert response[0].get("vhost") == "test"


def test_start_vhost(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.post(url__regex="vhosts/test/start/test%40rabbitmq").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    management_api.vhosts.start(vhost="test", node="test@rabbitmq")


def test_get_vhost_channels(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("vhosts/test/channels").respond(text='[{"running": true}]')

    response = management_api.vhosts.channels(vhost="test")

    assert isinstance(response, list)
    assert response[0].get("running") is True


def test_get_vhost_connections(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test/connections").respond(text='[{"state": "running"}]')

    response = management_api.vhosts.connections(vhost="test")

    assert isinstance(response, list)
    assert response[0].get("state") == "running"


def test_get_vhosts_limits(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("vhost-limits").respond(text='[{"vhost": "test"}]')

    response = management_api.vhosts.limits()

    assert isinstance(response, list)
    assert response[0].get("vhost") == "test"


def test_get_vhost_limits(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("vhost-limits/test").respond(text='[{"vhost": "test"}]')

    response = management_api.vhosts.vhost_limits(vhost="test")

    assert isinstance(response, list)
    assert response[0].get("vhost") == "test"


def test_set_vhost_limit(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.put("vhost-limits/test/max-queues", json={"value": 100}).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    management_api.vhosts.set_limit(vhost="test", limit="max-queues", value=100)


def test_delete_vhost_limit(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete("vhost-limits/test/max-queues").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    management_api.vhosts.delete_limit(vhost="test", limit="max-queues")
