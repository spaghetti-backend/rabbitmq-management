import pytest
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_all_nodes(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("nodes").respond(text='[{"name": "test@rabbitmq", "running": true}]')

    response = await async_management_api.nodes.all()

    assert isinstance(response, list)
    assert response[0].get("name") == "test@rabbitmq"


@pytest.mark.parametrize(
    "memory, binary",
    [
        (False, False),
        (True, False),
        (False, True),
        (True, True),
    ],
)
async def test_get_node_detail(
    memory: bool,
    binary: bool,
    async_management_api: api.AsyncRMQManagementAPI,
    api_mock: MockRouter,
):
    params = {}
    if memory:
        params["memory"] = True
    if binary:
        params["binary"] = True

    api_mock.get(url__regex="nodes/test%40rabbitmq", params=params).respond(
        text='{"name": "test@rabbitmq"}'
    )

    response = await async_management_api.nodes.detail(
        node="test@rabbitmq", memory=memory, binary=binary
    )

    assert response.get("name") == "test@rabbitmq"
