import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_all_exchanges(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("exchanges").respond(text='[{"name": "test"}]')

    response = await async_management_api.exchanges.all()

    assert isinstance(response, list)


async def test_get_exchanges_by_vhost(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F").respond(text='[{"name": "test"}]')

    response = await async_management_api.exchanges.by_vhost(vhost="/")

    assert isinstance(response, list)


async def test_get_exchange_details(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F/test").respond(text='{"name": "test"}')

    response = await async_management_api.exchanges.detail(vhost="/", exchange="test")

    assert response.get("name") == "test"


async def test_create_exchange(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.put(
        url__regex="exchanges/%2F/new_exch",
        json={
            "type": "direct",
            "auto_delete": False,
            "durable": True,
            "internal": False,
            "arguments": {"x-arg": "value"},
        },
    ).respond(status_code=httpx.codes.CREATED)

    await async_management_api.exchanges.create(
        vhost="/",
        exchange="new_exch",
        exchange_type="direct",
        auto_delete=False,
        durable=True,
        internal=False,
        arguments={"x-arg": "value"},
    )


async def test_delete_exchange(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(
        url__regex="exchanges/%2F/test", params={"if-unused": True}
    ).respond(status_code=httpx.codes.NO_CONTENT)

    await async_management_api.exchanges.delete(
        vhost="/", exchange="test", if_unused=True
    )


async def test_get_exchanges_source_bindings(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F/test/bindings/source").respond(
        text='[{"source": "test"}]'
    )

    response = await async_management_api.exchanges.source_bindings(
        vhost="/", exchange="test"
    )

    assert isinstance(response, list)


async def test_get_exchanges_distination_bindings(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F/test/bindings/destination").respond(
        text='[{"destination": "test"}]'
    )

    response = await async_management_api.exchanges.destination_bindings(
        vhost="/", exchange="test"
    )

    assert isinstance(response, list)
