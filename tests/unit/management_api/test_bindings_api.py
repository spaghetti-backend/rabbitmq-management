from typing import Optional

import httpx
import pytest
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_all_bindings(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("bindings").respond(
        text='[{"routing_key": "test"}, {"routing_key": "dev"}]'
    )

    response = management_api.bindings.all()

    assert isinstance(response, list)


def test_get_bindings_by_vhost(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="bindings/%2F").respond(
        text='[{"routing_key": "test"}, {"routing_key": "dev"}]'
    )

    response = management_api.bindings.by_vhost(vhost="/")

    assert isinstance(response, list)


def test_get_exchange_to_queue_bindings(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="bindings/%2F/e/te/q/tq").respond(
        text='[{"source": "te", "destination": "tq"}]'
    )

    response = management_api.bindings.exchange_to_queue(
        vhost="/", exchange="te", queue="tq"
    )

    assert isinstance(response, list)


@pytest.mark.parametrize(
    "routing_key, arguments",
    [
        (None, None),
        ("test", None),
        (None, {"x-match": "any"}),
        ("test", {"x-match": "any"}),
    ],
)
def test_create_exchange_to_queue_binding(
    routing_key: Optional[str],
    arguments: Optional[dict],
    management_api: api.RMQManagementAPI,
    api_mock: MockRouter,
):
    location = ""
    mock_json = {}
    if routing_key:
        mock_json["routing_key"] = routing_key
        location += routing_key
    if arguments:
        mock_json["arguments"] = arguments
        location += "~Ft5er"

    if not location:
        location = "~"

    api_mock.post(url__regex="bindings/%2F/e/te/q/nq", json=mock_json).respond(
        status_code=httpx.codes.CREATED, headers={"location": location}
    )

    response = management_api.bindings.bind_exchange_to_queue(
        vhost="/",
        exchange="te",
        queue="nq",
        routing_key=routing_key,
        arguments=arguments,
    )

    assert response == location


def test_get_exchange_to_queue_binding_details(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="bindings/%2F/e/te/q/tq/~").respond(
        text='{"source": "te", "destination": "tq", "properties_key": "~"}'
    )

    response = management_api.bindings.exchange_to_queue_binding_details(
        vhost="/", exchange="te", queue="tq", properties_key="~"
    )

    assert response.get("properties_key") == "~"


def test_unbind_exchange_from_queue(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(url__regex="bindings/%2F/e/te/q/tq/~").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.bindings.unbind_exchange_from_queue(
        vhost="/", exchange="te", queue="tq", properties_key="~"
    )

    assert response is None


def test_get_exchange_to_exchange_bindings(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="bindings/%2F/e/te/e/ae").respond(
        text='[{"source": "te", "destination": "ae"}]'
    )

    response = management_api.bindings.exchange_to_exchange(
        vhost="/", source="te", destination="ae"
    )

    assert isinstance(response, list)


@pytest.mark.parametrize(
    "routing_key, arguments",
    [
        (None, None),
        ("test", None),
        (None, {"x-match": "any"}),
        ("test", {"x-match": "any"}),
    ],
)
def test_create_exchange_to_exchange_binding(
    routing_key: Optional[str],
    arguments: Optional[dict],
    management_api: api.RMQManagementAPI,
    api_mock: MockRouter,
):
    location = ""
    mock_json = {}
    if routing_key:
        mock_json["routing_key"] = routing_key
        location += routing_key
    if arguments:
        mock_json["arguments"] = arguments
        location += "~Ft5er"

    if not location:
        location = "~"

    api_mock.post(url__regex="bindings/%2F/e/te/e/ae", json=mock_json).respond(
        status_code=httpx.codes.CREATED, headers={"location": location}
    )

    response = management_api.bindings.bind_exchange_to_exchange(
        vhost="/",
        source="te",
        destination="ae",
        routing_key=routing_key,
        arguments=arguments,
    )

    assert response == location


def test_get_exchange_to_exchange_binding_details(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="bindings/%2F/e/te/e/ae/~").respond(
        text='{"source": "te", "destination": "ae", "properties_key": "~"}'
    )

    response = management_api.bindings.exchange_to_exchange_binding_details(
        vhost="/", source="te", destination="ae", properties_key="~"
    )

    assert response.get("properties_key") == "~"


def test_unbind_exchange_from_exchange(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(url__regex="bindings/%2F/e/te/e/ae/~").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.bindings.unbind_exchange_from_exchange(
        vhost="/", source="te", destination="ae", properties_key="~"
    )

    assert response is None
