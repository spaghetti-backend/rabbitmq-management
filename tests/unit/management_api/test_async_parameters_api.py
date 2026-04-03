import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


async def test_get_all_parameters(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("parameters").respond(text='[{"name": "test", "value": 10}]')

    response = await async_management_api.parameters.all()

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_get_component_parameters(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("parameters/shovel").respond(text='[{"component": "shovel"}]')

    response = await async_management_api.parameters.by_component(component="shovel")

    assert isinstance(response, list)
    assert response[0].get("component") == "shovel"


async def test_get_vhosts_component_parameters(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="parameters/shovel/%2F").respond(
        text='[{"component": "shovel"}]'
    )

    response = await async_management_api.parameters.component_by_vhost(
        component="shovel", vhost="/"
    )

    assert isinstance(response, list)
    assert response[0].get("component") == "shovel"


async def test_get_component_parameter_detail(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="parameters/shovel/%2F/test").respond(
        text='{"component": "shovel"}'
    )

    response = await async_management_api.parameters.detail(
        component="shovel", vhost="/", parameter="test"
    )

    assert response.get("component") == "shovel"


async def test_set_component_parameter(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    mock_json = {
        "value": {
            "ack-mode": "on-confirm",
            "dest-add-forward-headers": False,
            "dest-protocol": "amqp091",
            "dest-queue": "test",
            "dest-uri": "amqp://",
            "src-delete-after": "never",
            "src-protocol": "amqp091",
            "src-queue": "test",
            "src-uri": "amqp://",
        },
        "vhost": "/",
        "component": "shovel",
        "name": "test",
    }
    api_mock.put(
        url__regex="parameters/shovel/%2F/test",
        json=mock_json,
    ).respond(status_code=httpx.codes.CREATED)

    await async_management_api.parameters.set(
        component="shovel", vhost="/", parameter="test", value=mock_json.get("value")
    )


async def test_delete_parameter(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(url__regex="parameters/shovel/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.parameters.delete(
        component="shovel", vhost="/", parameter="test"
    )


async def test_get_all_global_parameters(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("global-parameters").respond(text='[{"name": "test", "value": 10}]')

    response = await async_management_api.parameters.global_parameters()

    assert isinstance(response, list)
    assert response[0].get("name") == "test"


async def test_get_global_parameter_detail(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="global-parameters/test").respond(
        text='{"name": "test", "value": 10}'
    )

    response = await async_management_api.parameters.global_parameter_detail(
        parameter="test"
    )

    assert response.get("name") == "test"


async def test_set_global_parameter(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    mock_json = {
        "name": "test",
        "value": {"guest": "/", "rabbit": "warren"},
    }
    api_mock.put(
        url__regex="global-parameters/test",
        json=mock_json,
    ).respond(status_code=httpx.codes.CREATED)

    await async_management_api.parameters.set_global_parameter(
        parameter="test", value=mock_json.get("value")
    )


async def test_delete_global_parameter(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(url__regex="parameters/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    await async_management_api.parameters.delete_global_parameter(parameter="test")
