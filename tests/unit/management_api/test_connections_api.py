from typing import Optional

import httpx
import pytest
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_all_connections(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections").respond(text='[{"state": "running"}]')

    response = management_api.connections.all()

    assert isinstance(response, list)


def test_get_connection_detail(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections/tc").respond(text='{"state": "running"}')

    response = management_api.connections.detail(connection="tc")

    assert response.get("state") == "running"


@pytest.mark.parametrize("reason", [None, "test"])
def test_close_connection(
    reason: Optional[str],
    management_api: api.RMQManagementAPI,
    api_mock: MockRouter,
):
    headers = {"X-Reason": reason} if reason else {}

    api_mock.delete("connections/tc", headers=headers).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    management_api.connections.close(connection="tc", reason=reason)


def test_connections_by_user(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections/username/tu").respond(text='[{"user": "tu"}]')

    response = management_api.connections.by_user(username="tu")

    assert isinstance(response, list)


@pytest.mark.parametrize("reason", [None, "test"])
def test_close_all_user_connections(
    reason: Optional[str],
    management_api: api.RMQManagementAPI,
    api_mock: MockRouter,
):
    headers = {"X-Reason": reason} if reason else {}

    api_mock.delete("connections/username/tu", headers=headers).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    management_api.connections.close_user_connections(username="tu", reason=reason)


def test_get_connection_channels(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("connections/tu/channels").respond(text='[{"state": "running"}]')

    response = management_api.connections.channels(connection="tu")

    assert isinstance(response, list)
