import httpx
from respx import MockRouter

from rabbitmq_management import management_api as api


def test_get_all_policies(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get("policies").respond(text='[{"name": "test"}]')

    response = management_api.policies.all()

    assert isinstance(response, list)


def test_get_policies_by_vhost(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="policies/%2F").respond(text='[{"name": "test"}]')

    response = management_api.policies.by_vhost(vhost="/")

    assert isinstance(response, list)


def test_get_policy_detail(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.get(url__regex="policies/%2F/test").respond(text='{"name": "test"}')

    response = management_api.policies.detail(vhost="/", policy="test")

    assert response.get("name") == "test"


def test_set_policy(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    mock_json = {
        "pattern": "^amq.",
        "definition": {"federation-upstream-set": "all"},
        "priority": 0,
        "apply-to": "all",
    }
    api_mock.put(url__regex="policies/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.policies.set(vhost="/", policy="test", value=mock_json)

    assert response is None


def test_delete_policy(management_api: api.RMQManagementAPI, api_mock: MockRouter):
    api_mock.delete(url__regex="policies/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.policies.delete(vhost="/", policy="test")

    assert response is None


def test_get_all_operator_policies(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("operator-policies").respond(text='[{"name": "test"}]')

    response = management_api.policies.operator.all()

    assert isinstance(response, list)


def test_get_operator_policies_by_vhost(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="operator-policies/%2F").respond(text='[{"name": "test"}]')

    response = management_api.policies.operator.by_vhost(vhost="/")

    assert isinstance(response, list)


def test_get_operator_policy_detail(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.get(url__regex="operator-policies/%2F/test").respond(
        text='{"name": "test"}'
    )

    response = management_api.policies.operator.detail(vhost="/", policy="test")

    assert response.get("name") == "test"


def test_set_operator_policy(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    mock_json = {
        "pattern": "^amq.",
        "definition": {"expires": 100},
        "priority": 0,
        "apply-to": "queues",
    }
    api_mock.put(url__regex="operator-policies/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.policies.operator.set(
        vhost="/", policy="test", value=mock_json
    )

    assert response is None


def test_delete_operator_policy(
    management_api: api.RMQManagementAPI, api_mock: MockRouter
):
    api_mock.delete(url__regex="operator-policies/%2F/test").respond(
        status_code=httpx.codes.NO_CONTENT
    )

    response = management_api.policies.operator.delete(vhost="/", policy="test")

    assert response is None
