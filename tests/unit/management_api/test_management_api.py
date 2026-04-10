import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_aliveness(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get(url__regex="aliveness-test/%2F").respond(text='{"status": "ok"}')

    response = management_api.aliveness_test("/")

    assert response.get("status") == "ok"


def test_get_cluster_name(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("cluster-name").respond(text='{"name": "rabbit@rabbitmq"}')

    response = management_api.cluster_name()

    assert response.get("name") == "rabbit@rabbitmq"


def test_change_cluster_name(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.put("cluster-name", json={"name": "test@rabbitmq"}).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.change_cluster_name("test@rabbitmq")

    assert response is None


def test_get_extensions(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("extensions").respond(
        text='[{"javascript": "dispatcher.js"},{"javascript": "federation.js"}]'
    )

    response = management_api.extensions()

    assert isinstance(response, list)


def test_get_overview(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("overview").respond(text='{"rabbitmq_version": "3.12.0"}')

    response = management_api.overview()

    assert "rabbitmq_version" in response


def test_rebalance_queues(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.post("rebalance/queues").respond(status_code=httpx.codes.NO_CONTENT)

    response = management_api.rebalance_queues()

    assert response is None


def test_whoami(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("whoami").respond(text='{"name": "guest","tags": ["administrator"]}')

    response = management_api.whoami()

    assert response.get("name") == "guest"
