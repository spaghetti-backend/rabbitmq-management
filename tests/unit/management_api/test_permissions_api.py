import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_all_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("permissions").respond(text='[{"user": "test"}]')

    response = management_api.permissions.all()

    assert isinstance(response, list)


def test_get_user_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="permissions/%2F/test").respond(text='{"user": "test"}')

    response = management_api.permissions.detail(vhost="/", user="test")

    assert response.get("user") == "test"


def test_set_permissions(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    mock_json = {"configure": ".*", "write": ".*", "read": ".*"}
    api_mock.put(url__regex="permissions/%2F/test", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.permissions.set(vhost="/", user="test", value=mock_json)

    assert response is None


def test_delete_permissions(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete(url__regex="permissions/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.permissions.delete(vhost="/", user="test")

    assert response is None


def test_get_all_topic_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("topic-permissions").respond(text='[{"user": "test"}]')

    response = management_api.permissions.topic.all()

    assert isinstance(response, list)


def test_get_user_topic_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="topic-permissions/%2F/test").respond(
        text='{"user": "test"}'
    )

    response = management_api.permissions.topic.detail(vhost="/", user="test")

    assert response.get("user") == "test"


def test_set_topic_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    mock_json = {"exchange": "amq.topic", "write": "^a", "read": ".*"}
    api_mock.put(url__regex="topic-permissions/%2F/test", json=mock_json).respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.permissions.topic.set(
        vhost="/", user="test", value=mock_json
    )

    assert response is None


def test_delete_topic_permissions(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(url__regex="topic-permissions/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.permissions.topic.delete(vhost="/", user="test")

    assert response is None
