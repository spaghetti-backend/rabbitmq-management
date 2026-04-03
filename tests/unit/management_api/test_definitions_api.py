import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_all_definitions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("definitions").respond(text='{"users": [{"name": "guest"}]}')

    response = management_api.definitions.all()

    assert response["users"][0]["name"] == "guest"


def test_upload_broker_definitions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    mock_json = {"vhosts": [{"name": "test"}]}
    api_mock.post("definitions", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    management_api.definitions.upload(definitions=mock_json)


def test_get_all_definitions_by_vhost(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="definitions/%2F").respond(
        text='{"queues": [{"name": "test"}]}'
    )

    response = management_api.definitions.by_vhost(vhost="/")

    assert response["queues"][0]["name"] == "test"


def test_upload_vhosts_definitions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    mock_json = {"queues": [{"name": "test", "durable": True}]}
    api_mock.post(url__regex="definitions/%2F", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    management_api.definitions.upload_vhosts_definitions(
        vhost="/", definitions=mock_json
    )
