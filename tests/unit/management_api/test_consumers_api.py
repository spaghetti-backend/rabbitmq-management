from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_consumers(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("consumers").respond(text='[{"active": true}]')

    response = management_api.consumers.all()

    assert isinstance(response, list)


def test_get_consumers_by_vhost(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="consumers/%2F").respond(text='[{"active": true}]')

    response = management_api.consumers.by_vhost("/")

    assert isinstance(response, list)
