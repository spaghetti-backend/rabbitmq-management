import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_all_exchanges(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("exchanges").respond(text='[{"name": "test"}]')

    response = management_api.exchanges.all()

    assert isinstance(response, list)


def test_get_exchanges_by_vhost(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F").respond(text='[{"name": "test"}]')

    response = management_api.exchanges.by_vhost(vhost="/")

    assert isinstance(response, list)


def test_get_exchange_details(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F/test").respond(text='{"name": "test"}')

    response = management_api.exchanges.detail(vhost="/", exchange="test")

    assert response.get("name") == "test"


def test_create_exchange(management_api: api.RMQManagementAPI, api_mock: MockRouter):
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

    response = management_api.exchanges.set(
        vhost="/",
        exchange="new_exch",
        exchange_type="direct",
        auto_delete=False,
        durable=True,
        internal=False,
        arguments={"x-arg": "value"},
    )

    assert response is None


def test_delete_exchange(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete(
        url__regex="exchanges/%2F/test", params={"if-unused": True}
    ).respond(status_code=httpx.codes.NO_CONTENT)

    response = management_api.exchanges.delete(
        vhost="/", exchange="test", if_unused=True
    )

    assert response is None


def test_get_exchanges_source_bindings(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F/test/bindings/source").respond(
        text='[{"source": "test"}]'
    )

    response = management_api.exchanges.source_bindings(vhost="/", exchange="test")

    assert isinstance(response, list)


def test_get_exchanges_distination_bindings(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="exchanges/%2F/test/bindings/destination").respond(
        text='[{"destination": "test"}]'
    )

    response = management_api.exchanges.destination_bindings(vhost="/", exchange="test")

    assert isinstance(response, list)
