import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_attempts(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get(url__regex="auth/attempts/test%40rabbitmq").respond(
        text='[{"protocol": "http"}]'
    )

    response = management_api.auth.attempts("test@rabbitmq")

    assert isinstance(response, list)


def test_reset_attempts(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete(url__regex="auth/attempts/test%40rabbitmq").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.auth.reset_attempts("test@rabbitmq")

    assert response is None


def test_get_attempts_by_source(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="auth/attempts/test%40rabbitmq/source").respond(
        text='[{"remote_address": "172.23.0.1"}]'
    )

    response = management_api.auth.attempts_by_source("test@rabbitmq")

    assert isinstance(response, list)


def test_get_attempts_by_source_when_tracking_disabled(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="auth/attempts/test%40rabbitmq/source").respond(text="[]")

    response = management_api.auth.attempts_by_source("test@rabbitmq")

    assert isinstance(response, list)
    assert len(response) == 0


def test_reset_attempts_by_source(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(url__regex="auth/attempts/test%40rabbitmq/source").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.auth.reset_attempts_by_source("test@rabbitmq")

    assert response is None


def test_auth_detail(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("auth").respond(text='{"oauth_enabled": false}')

    response = management_api.auth.detail()

    assert response.get("oauth_enabled") is False


def test_hash_password(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("auth/hash_password/password").respond(
        text='{"ok": "OSMSKkVu/rOYMST65zoHT9bB9IBvTlYc9AQSXh4Sk5HZu3uu"}'
    )

    response = management_api.auth.hash_password("password")

    assert response.get("ok") == "OSMSKkVu/rOYMST65zoHT9bB9IBvTlYc9AQSXh4Sk5HZu3uu"
