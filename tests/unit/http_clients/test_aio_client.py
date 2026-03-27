import pytest
from rabbitmq_management import _http_clients as client
import respx
import httpx

from rabbitmq_management._exceptions import (
    RMQApiError,
    RMQNetworkError,
    RMQRequestError,
)


async def test_get_succuss(async_http_client: client.AsyncHTTPClient, api_url: str):
    with respx.mock:
        respx.get(f"{api_url}/api/overview").respond(
            status_code=httpx.codes.OK,
            text='{"rabbitmq_version": "3.12.0"}',
        )

        response = await async_http_client.get("overview")

        assert response.get("rabbitmq_version") == "3.12.0"


async def test_succuss_with_no_content(
    async_http_client: client.AsyncHTTPClient, api_url: str
):
    with respx.mock:
        respx.delete(f"{api_url}/api/users/test").respond(
            status_code=httpx.codes.NO_CONTENT,
        )

        response = await async_http_client.delete("users/test")

        assert response.get("status") == "success"


async def test_timeout_wraps_with_rmq_network_error(
    async_http_client: client.AsyncHTTPClient, api_url: str
):
    with respx.mock:
        respx.put(f"{api_url}/api/users/test").mock(
            side_effect=httpx.TimeoutException("Timeout")
        )

        with pytest.raises(RMQNetworkError, match="Request timed out"):
            await async_http_client.put(
                "users/test", payload={"password": "test", "tags": "management"}
            )


async def test_connect_error_wraps_with_rmq_network_error(
    async_http_client: client.AsyncHTTPClient, api_url: str
):
    with respx.mock:
        respx.post(f"{api_url}/api/users/bulk-delete").mock(
            side_effect=httpx.ConnectError("ConnectError")
        )

        with pytest.raises(RMQNetworkError, match="Network connection failed"):
            await async_http_client.post(
                "users/bulk-delete", payload={"users": ["test"]}
            )


async def test_request_errors_wraps_with_rmq_request_error(
    async_http_client: client.AsyncHTTPClient, api_url: str
):
    with respx.mock:
        respx.get(f"{api_url}/api/overview").mock(
            side_effect=httpx.DecodingError("DecodingError")
        )

        with pytest.raises(RMQRequestError, match="Request failed"):
            await async_http_client.get("overview")


async def test_api_errors_wraps_with_rmq_api_error(
    async_http_client: client.AsyncHTTPClient, api_url: str
):
    with respx.mock:
        respx.delete(f"{api_url}/api/users/test").mock(
            return_value=respx.MockResponse(
                status_code=httpx.codes.NOT_FOUND,
                content='{"error": "Object Not Found", "reason": "Not Found"}',
            ),
        )

        with pytest.raises(RMQApiError, match="Object Not Found"):
            await async_http_client.delete("users/test")
