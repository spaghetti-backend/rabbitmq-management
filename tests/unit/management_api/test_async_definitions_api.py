import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_all_definitions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("definitions").respond(text='{"users": [{"name": "guest"}]}')

    response = await async_management_api.definitions.all()

    assert response["users"][0]["name"] == "guest"


async def test_upload_broker_definitions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    mock_json = {"vhosts": [{"name": "test"}]}
    api_mock.post("definitions", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = await async_management_api.definitions.upload(definitions=mock_json)

    assert response is None


async def test_get_all_definitions_by_vhost(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="definitions/%2F").respond(
        text='{"queues": [{"name": "test"}]}'
    )

    response = await async_management_api.definitions.by_vhost(vhost="/")

    assert response["queues"][0]["name"] == "test"


async def test_upload_vhosts_definitions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    mock_json = {"queues": [{"name": "test", "durable": True}]}
    api_mock.post(url__regex="definitions/%2F", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = await async_management_api.definitions.upload_vhosts_definitions(
        vhost="/", definitions=mock_json
    )

    assert response is None
