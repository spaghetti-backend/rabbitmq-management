import httpx
import pytest
from respx import MockRouter

from rabbitmq_management import management_api as api


@pytest.mark.parametrize(
    "enable_queue_totals, disable_stats",
    [
        (False, False),
        (True, False),
        (False, True),
        (True, True),
    ],
)
def test_get_all_queues(
    enable_queue_totals: bool,
    disable_stats: bool,
    management_api: api.RMQManagementAPI,
    api_mock: MockRouter,
):
    params = {}
    if enable_queue_totals:
        params["enable_queue_totals"] = enable_queue_totals
    if disable_stats:
        params["disable_stats"] = disable_stats

    api_mock.get("queues", params=params).respond(text='[{"name": "test"}]')

    response = management_api.queues.all(
        enable_queue_totals=enable_queue_totals, disable_stats=disable_stats
    )

    assert isinstance(response, list)


def test_get_all_queues_by_vhost(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="queues/%2F").respond(text='[{"name": "test"}]')

    response = management_api.queues.by_vhost(vhost="/")

    assert isinstance(response, list)


def test_get_queue_detail(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get(url__regex="queues/%2F/test").respond(text='{"name": "test"}')

    response = management_api.queues.detail(vhost="/", queue="test")

    assert response.get("name") == "test"


def test_set_queue(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    mock_json = {
        "auto_delete": False,
        "durable": True,
        "arguments": {},
        "node": "test@rabbitmq",
    }
    api_mock.put(url__regex="queues/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.queues.set(vhost="/", queue="test", value=mock_json)

    assert response is None


def test_delete_queue(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete(url__regex="queues/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.queues.delete(vhost="/", queue="test")

    assert response is None


def test_get_queue_bindings(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get(url__regex="queues/%2F/test/bindings").respond(
        text='[{"destination": "test"}]'
    )

    response = management_api.queues.bindings(vhost="/", queue="test")

    assert isinstance(response, list)


def test_purge_queue(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete(url__regex="queues/%2F/test/contents").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.queues.purge(vhost="/", queue="test")

    assert response is None


def test_queue_action(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    mock_json = {"action": "sync"}
    api_mock.post(url__regex="queues/%2F/test/actions", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.queues.actions(vhost="/", queue="test", value=mock_json)

    assert response is None


def test_get_message_from_queue(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    mock_json = {
        "count": 5,
        "ackmode": "ack_requeue_true",
        "encoding": "auto",
        "truncate": 50000,
    }
    api_mock.post(url__regex="queues/%2F/test/get", json=mock_json).respond(
        text='[{"payload": "test"}]'
    )

    response = management_api.queues.messages(vhost="/", queue="test", value=mock_json)

    assert isinstance(response, list)
