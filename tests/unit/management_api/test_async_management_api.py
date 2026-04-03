import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_aliveness(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="aliveness-test/%2F").respond(text='{"status": "ok"}')

    response = await async_management_api.aliveness_test("/")

    assert response.get("status") == "ok"


async def test_get_cluster_name(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("cluster-name").respond(text='{"name": "rabbit@rabbitmq"}')

    response = await async_management_api.cluster_name()

    assert response.get("name") == "rabbit@rabbitmq"


async def test_change_cluster_name(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.put("cluster-name", json={"name": "test@rabbitmq"}).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.change_cluster_name("test@rabbitmq")


async def test_get_extensions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("extensions").respond(
        text='[{"javascript": "dispatcher.js"},{"javascript": "federation.js"},{"javascript": "shovel.js"}]'
    )

    response = await async_management_api.extensions()

    assert isinstance(response, list)
    assert len(response) == 3
    assert response[0].get("javascript") == "dispatcher.js"


async def test_get_overview(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("overview").respond(text='{"rabbitmq_version": "3.12.0"}')

    response = await async_management_api.overview()

    assert "rabbitmq_version" in response


async def test_rebalance_queues(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.post("rebalance/queues").respond(status_code=httpx.codes.NO_CONTENT)

    await async_management_api.rebalance_queues()


async def test_whoami(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("whoami").respond(text='{"name": "guest","tags": ["administrator"]}')

    response = await async_management_api.whoami()

    assert response.get("name") == "guest"
