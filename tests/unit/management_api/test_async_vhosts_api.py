import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_all_vhosts(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts").respond(text='[{"name": "test"}]')

    response = await async_management_api.vhosts.all()

    assert isinstance(response, list)


async def test_get_vhost_detail(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test").respond(text='{"name": "test"}')

    response = await async_management_api.vhosts.detail(vhost="test")

    assert response.get("name") == "test"


async def test_set_vhost(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    mock_json = {
        "description": "virtual host description",
        "tags": "accounts,production",
        "tracing": True,
    }
    api_mock.put("vhosts/test").respond(status_code=httpx.codes.NO_CONTENT)

    response = await async_management_api.vhosts.set(vhost="test", value=mock_json)

    assert response is None


async def test_delete_vhost(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete("vhosts/test").respond(status_code=httpx.codes.NO_CONTENT)

    response = await async_management_api.vhosts.delete(vhost="test")

    assert response is None


async def test_get_vhost_permissions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test/permissions").respond(text='[{"vhost": "test"}]')

    response = await async_management_api.vhosts.permissions(vhost="test")

    assert isinstance(response, list)


async def test_get_vhost_topic_permissions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test/topic-permissions").respond(text='[{"vhost": "test"}]')

    response = await async_management_api.vhosts.topic_permissions(vhost="test")

    assert isinstance(response, list)


async def test_start_vhost(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.post(url__regex="vhosts/test/start/test%40rabbitmq").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = await async_management_api.vhosts.start(
        vhost="test", node="test@rabbitmq"
    )

    assert response is None


async def test_get_vhost_channels(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test/channels").respond(text='[{"running": true}]')

    response = await async_management_api.vhosts.channels(vhost="test")

    assert isinstance(response, list)


async def test_get_vhost_connections(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhosts/test/connections").respond(text='[{"state": "running"}]')

    response = await async_management_api.vhosts.connections(vhost="test")

    assert isinstance(response, list)


async def test_get_vhosts_limits(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhost-limits").respond(text='[{"vhost": "test"}]')

    response = await async_management_api.vhosts.limits()

    assert isinstance(response, list)


async def test_get_vhost_limits(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("vhost-limits/test").respond(text='[{"vhost": "test"}]')

    response = await async_management_api.vhosts.vhost_limits(vhost="test")

    assert isinstance(response, list)


async def test_set_vhost_limit(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.put("vhost-limits/test/max-queues", json={"value": 100}).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = await async_management_api.vhosts.set_limit(
        vhost="test", limit="max-queues", value=100
    )

    assert response is None


async def test_delete_vhost_limit(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete("vhost-limits/test/max-queues").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = await async_management_api.vhosts.delete_limit(
        vhost="test", limit="max-queues"
    )

    assert response is None
