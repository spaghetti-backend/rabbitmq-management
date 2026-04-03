import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_all_users(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("users").respond(text='[{"name": "test"}]')

    response = await async_management_api.users.all()

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_get_users_without_permissions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("users/without-permissions").respond(text='[{"name": "test"}]')

    response = await async_management_api.users.without_permissions()

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_bulk_delete_users(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    mock_json = {"users": ["user1", "user2", "user3"]}
    api_mock.post("users/bulk-delete", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.users.bulk_delete(value=mock_json)


async def test_get_user_detail(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("users/test").respond(text='{"name": "test"}')

    response = await async_management_api.users.detail(user="test")

    assert response.get("name") == "test"


async def test_set_user(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    mock_json = {"password": "secret", "tags": "administrator"}
    api_mock.put("users/test").respond(status_code=httpx.codes.NO_CONTENT)

    await async_management_api.users.set(user="test", value=mock_json)


async def test_delete_user(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete("users/test").respond(status_code=httpx.codes.NO_CONTENT)

    await async_management_api.users.delete(user="test")


async def test_get_user_permissions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("users/test/permissions").respond(text='[{"name": "test"}]')

    response = await async_management_api.users.permissions(user="test")

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_get_user_topic_permissions(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("users/test/topic-permissions").respond(text='[{"name": "test"}]')

    response = await async_management_api.users.topic_permissions(user="test")

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_get_all_users_limits(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("user-limits").respond(text='[{"name": "test"}]')

    response = await async_management_api.users.limits()

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_get_user_limits(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("user-limits/test").respond(text='[{"name": "test"}]')

    response = await async_management_api.users.individual_limits(user="test")

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_set_user_limit(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.put("user-limits/test/max-channels", json={"value": 100}).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.users.set_limit(
        user="test", limit="max-channels", value=100
    )


async def test_delete_user_limit(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete("user-limits/test/max-channels").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.users.delete_limit(user="test", limit="max-channels")
