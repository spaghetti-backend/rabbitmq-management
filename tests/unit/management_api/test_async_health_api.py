import httpx
import pytest
from respx import MockRouter

from rabbitmq_management import management_api as api
from rabbitmq_management.exceptions import RMQApiError


async def test_check_no_alarms(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/alarms").respond(text='{"status": "ok"}')

    response = await async_management_api.health.alarms()

    assert response.get("status") == "ok"


async def test_check_alarms_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/alarms").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE, text='{"status": "failed"}'
    )

    response = await async_management_api.health.alarms()

    assert response.get("status") == "failed"


async def test_check_alarms_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/alarms").respond(
        status_code=httpx.codes.BAD_REQUEST, text="test"
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.alarms()

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == "test"
    assert exc_info.value.reason is None


async def test_check_no_local_alarms(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/local-alarms").respond(text='{"status": "ok"}')

    response = await async_management_api.health.local_alarms()

    assert response.get("status") == "ok"


async def test_check_local_alarms_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/local-alarms").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE, text='{"status": "failed"}'
    )

    response = await async_management_api.health.local_alarms()

    assert response.get("status") == "failed"


async def test_check_local_alarms_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/local-alarms").respond(
        status_code=httpx.codes.BAD_REQUEST, text="test"
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.local_alarms()

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == "test"
    assert exc_info.value.reason is None


async def test_check_certificate_expiration(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/certificate-expiration/2/months").respond(
        text='{"status": "ok"}'
    )

    response = await async_management_api.health.certificate_expiration(
        within=2, unit="months"
    )

    assert response.get("status") == "ok"


async def test_check_certificate_expiration_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/certificate-expiration/2/months").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE, text='{"status": "failed"}'
    )

    response = await async_management_api.health.certificate_expiration(
        within=2, unit="months"
    )

    assert response.get("status") == "failed"


async def test_check_certificate_expiration_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/certificate-expiration/2/months").respond(
        status_code=httpx.codes.BAD_REQUEST, text="test"
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.certificate_expiration(
            within=2, unit="months"
        )

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == "test"
    assert exc_info.value.reason is None


async def test_check_port_listener(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/port-listener/15672").respond(
        text='{"status": "ok", "port": 15672}'
    )

    response = await async_management_api.health.port_listener(port=15672)

    assert response.get("status") == "ok"
    assert response.get("port") == 15672


async def test_check_port_listener_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/port-listener/11111").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE,
        text='{"status": "failed", "missing": 11111}',
    )

    response = await async_management_api.health.port_listener(port=11111)

    assert response.get("status") == "failed"
    assert response.get("missing") == 11111


async def test_check_port_listener_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/port-listener/11111").respond(
        status_code=httpx.codes.BAD_REQUEST
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.port_listener(port=11111)

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == ""


async def test_check_protocol_listener(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/protocol-listener/mqtt").respond(
        text='{"status": "ok", "protocol": "mqtt"}'
    )

    response = await async_management_api.health.protocol_listener(protocol="mqtt")

    assert response.get("status") == "ok"
    assert response.get("protocol") == "mqtt"


async def test_check_protocol_listener_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/protocol-listener/mqtt").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE,
        text='{"status": "failed", "missing": "mqtt"}',
    )

    response = await async_management_api.health.protocol_listener(protocol="mqtt")

    assert response.get("status") == "failed"
    assert response.get("missing") == "mqtt"


async def test_check_protocol_listener_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/protocol-listener/mqtt").respond(
        status_code=httpx.codes.BAD_REQUEST
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.protocol_listener(protocol="mqtt")

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == ""


async def test_check_virtual_hosts(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/virtual-hosts").respond(text='{"status": "ok"}')

    response = await async_management_api.health.vhosts()

    assert response.get("status") == "ok"


async def test_check_virtual_hosts_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/virtual-hosts").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE,
        text='{"status": "failed"}',
    )

    response = await async_management_api.health.vhosts()

    assert response.get("status") == "failed"


async def test_check_virtual_hosts_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/virtual-hosts").respond(
        status_code=httpx.codes.BAD_REQUEST
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.vhosts()

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == ""


async def test_check_node_is_mirror_sync_critical(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/node-is-mirror-sync-critical").respond(
        text='{"status": "ok"}'
    )

    response = await async_management_api.health.has_critical_mirror_sync()

    assert response.get("status") == "ok"


async def test_check_node_is_mirror_sync_critical_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/node-is-mirror-sync-critical").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE,
        text='{"status": "failed"}',
    )

    response = await async_management_api.health.has_critical_mirror_sync()

    assert response.get("status") == "failed"


async def test_check_node_is_mirror_sync_critical_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/node-is-mirror-sync-critical").respond(
        status_code=httpx.codes.BAD_REQUEST
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.has_critical_mirror_sync()

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == ""


async def test_check_quorum_critical(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/node-is-quorum-critical").respond(
        text='{"status": "ok"}'
    )

    response = await async_management_api.health.node_quorum_critical()

    assert response.get("status") == "ok"


async def test_check_quorum_critical_with_error(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/node-is-quorum-critical").respond(
        status_code=httpx.codes.SERVICE_UNAVAILABLE,
        text='{"status": "failed"}',
    )

    response = await async_management_api.health.node_quorum_critical()

    assert response.get("status") == "failed"


async def test_check_quorum_critical_propagates_api_errors(
    async_management_api: api.AsyncRMQManagementAPI, api_mock: MockRouter
):
    api_mock.get("health/checks/node-is-quorum-critical").respond(
        status_code=httpx.codes.BAD_REQUEST
    )

    with pytest.raises(RMQApiError) as exc_info:
        await async_management_api.health.node_quorum_critical()

    assert exc_info.value.status_code == httpx.codes.BAD_REQUEST
    assert exc_info.value.text == ""
