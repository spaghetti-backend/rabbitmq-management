from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_channels(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("channels").respond(text='[{"state": "running"}]')

    response = await async_management_api.channels.all()

    assert isinstance(response, list)


async def test_get_channel_detail(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(
        url__regex="channels/172.23.0.1%3A54558%20-%3E%20172.23.0.2%3A5672%20%281%29"
    ).respond(text='{"state": "running"}')

    response = await async_management_api.channels.detail(
        "172.23.0.1:54558 -> 172.23.0.2:5672 (1)"
    )

    assert response.get("state") == "running"
