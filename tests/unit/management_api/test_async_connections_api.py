from typing import Optional
import httpx
import pytest
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_all_connections(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections").respond(text='[{"state": "running"}]')

    response = await async_management_api.connections.all()

    assert isinstance(response, list)


async def test_get_connection_detail(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections/tc").respond(text='{"state": "running"}')

    response = await async_management_api.connections.detail(connection="tc")

    assert response.get("state") == "running"


@pytest.mark.parametrize("reason", [None, "test"])
async def test_close_connection(
    reason: Optional[str],
    async_management_api: api.AsyncRMQManagementAPI,
    api_mock: MockRouter,
):
    if reason:
        headers = {"X-Reason": reason}
    else:
        headers = {}

    api_mock.delete("connections/tc", headers=headers).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.connections.close(connection="tc", reason=reason)


async def test_connections_by_user(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections/username/tu").respond(text='[{"user": "tu"}]')

    response = await async_management_api.connections.by_user(username="tu")

    assert isinstance(response, list)


@pytest.mark.parametrize("reason", [None, "test"])
async def test_close_all_user_connections(
    reason: Optional[str],
    async_management_api: api.AsyncRMQManagementAPI,
    api_mock: MockRouter,
):
    if reason:
        headers = {"X-Reason": reason}
    else:
        headers = {}

    api_mock.delete("connections/username/tu", headers=headers).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.connections.close_user_connections(
        username="tu", reason=reason
    )


async def test_get_connection_channels(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections/tu/channels").respond(text='[{"state": "running"}]')

    response = await async_management_api.connections.channels(connection="tu")

    assert isinstance(response, list)
