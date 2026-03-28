import httpx
import pytest
from respx import MockResponse, MockRouter

from rabbitmq_management import http_clients as client
from rabbitmq_management._exceptions import (
    RMQApiError,
    RMQNetworkError,
    RMQRequestError,
)


def test_get_succuss(http_client: client.HTTPClient, api_mock: MockRouter):
    api_mock.get("overview").respond(
        status_code=httpx.codes.OK,
        text='{"rabbitmq_version": "3.12.0"}',
    )

    response = http_client.get("overview")

    assert response.get("rabbitmq_version") == "3.12.0"


def test_succuss_with_no_content(http_client: client.HTTPClient, api_mock: MockRouter):
    api_mock.delete("users/test").respond(
        status_code=httpx.codes.NO_CONTENT,
    )

    response = http_client.delete("users/test")

    assert response.get("status") == "success"


def test_timeout_wraps_with_rmq_network_error(
    http_client: client.HTTPClient, api_mock: MockRouter
):
    api_mock.put("users/test").mock(side_effect=httpx.TimeoutException("Timeout"))

    with pytest.raises(RMQNetworkError, match="Request timed out"):
        http_client.put(
            "users/test", payload={"password": "test", "tags": "management"}
        )


def test_connect_error_wraps_with_rmq_network_error(
    http_client: client.HTTPClient, api_mock: MockRouter
):
    api_mock.post("users/bulk-delete").mock(
        side_effect=httpx.ConnectError("ConnectError")
    )

    with pytest.raises(RMQNetworkError, match="Network connection failed"):
        http_client.post("users/bulk-delete", payload={"users": ["test"]})


def test_request_errors_wraps_with_rmq_request_error(
    http_client: client.HTTPClient, api_mock: MockRouter
):
    api_mock.get("overview").mock(side_effect=httpx.DecodingError("DecodingError"))

    with pytest.raises(RMQRequestError, match="Request failed"):
        http_client.get("overview")


def test_api_errors_wraps_with_rmq_api_error(
    http_client: client.HTTPClient, api_mock: MockRouter
):
    api_mock.delete("users/test").mock(
        return_value=MockResponse(
            status_code=httpx.codes.NOT_FOUND,
            content='{"error": "Object Not Found", "reason": "Not Found"}',
        ),
    )

    with pytest.raises(RMQApiError, match="Object Not Found"):
        http_client.delete("users/test")
