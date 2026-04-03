from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_consumers(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("consumers").respond(text='[{"active": true}]')

    response = await async_management_api.consumers.all()

    assert isinstance(response, list)


async def test_get_consumers_by_vhost(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="consumers/%2F").respond(text='[{"active": true}]')

    response = await async_management_api.consumers.by_vhost("/")

    assert isinstance(response, list)
