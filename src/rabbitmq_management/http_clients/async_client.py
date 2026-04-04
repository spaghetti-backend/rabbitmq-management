from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

import httpx

from rabbitmq_management.exceptions import (
    RMQApiError,
    RMQNetworkError,
    RMQRequestError,
)

if TYPE_CHECKING:
    import ssl
    from types import TracebackType


CertTypes = Union[str, tuple[str, str], tuple[str, str, str]]


class AsyncHTTPClient:
    def __init__(
        self,
        api_url: str,
        username: str,
        password: str,
        *,
        timeout: float = 5.0,
        verify: ssl.SSLContext | str | bool = True,
        cert: CertTypes | None = None,
    ):
        credentials = httpx.BasicAuth(username=username, password=password)

        self.client = httpx.AsyncClient(
            auth=credentials,
            verify=verify,
            cert=cert,
            timeout=timeout,
            base_url=api_url,
        )

    async def __aenter__(self) -> AsyncHTTPClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException,
        tb: TracebackType,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self.client.aclose()

    async def _request(
        self,
        method: str,
        path: str,
        *,
        payload: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        try:
            request = self.client.build_request(
                method=method,
                url=path,
                json=payload,
                headers=headers,
            )
            response = await self.client.send(request)
            response.raise_for_status()

            if not response.content:
                return {"status": "success", "headers": response.headers}

            return response.json()
        except httpx.TimeoutException as e:
            raise RMQNetworkError(
                f"Request timed out while accessing RabbitMQ: {e}"
            ) from e

        except httpx.NetworkError as e:
            raise RMQNetworkError(
                f"Network connection failed or was dropped: {e}"
            ) from e

        except httpx.RequestError as e:
            raise RMQRequestError(f"Request failed: {e}") from e

        except httpx.HTTPStatusError as e:
            raise RMQApiError(
                message=f"RabbitMQ API returned an error ({e.response.status_code}): \
                {e.response.text}",
                status_code=e.response.status_code,
                text=e.response.text,
            ) from e

    async def get(self, path: str) -> Any:
        return await self._request("GET", path=path)

    async def post(self, path: str, payload: dict | None = None) -> Any:
        return await self._request("POST", path=path, payload=payload)

    async def put(self, path: str, payload: dict | None = None) -> dict:
        return await self._request("PUT", path=path, payload=payload)

    async def delete(self, path: str, *, headers: dict | None = None) -> dict:
        return await self._request("DELETE", path=path, headers=headers)
