from __future__ import annotations

from types import TracebackType
from typing import TYPE_CHECKING, Optional, Tuple, Type, Union

import httpx

from rabbitmq_management._exceptions import (
    RMQApiError,
    RMQNetworkError,
    RMQRequestError,
)

if TYPE_CHECKING:
    import ssl


CertTypes = Union[str, Tuple[str, str], Tuple[str, str, str]]


class HTTPClient:
    def __init__(
        self,
        api_url: str,
        username: str,
        password: str,
        *,
        timeout: float = 5.0,
        verify: Union[ssl.SSLContext, str, bool] = True,
        cert: Optional[CertTypes] = None,
    ):
        base_url = f"{api_url}/api/"
        credentials = httpx.BasicAuth(username=username, password=password)

        self.client = httpx.Client(
            auth=credentials,
            verify=verify,
            cert=cert,
            timeout=timeout,
            base_url=base_url,
        )

    def __enter__(self) -> HTTPClient:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: BaseException,
        tb: TracebackType,
    ) -> None:
        self.close()

    def close(self) -> None:
        self.client.close()

    def _request(
        self, method: str, path: str, *, payload: Optional[dict] = None
    ) -> dict:
        try:
            request = self.client.build_request(method=method, url=path, json=payload)
            response = self.client.send(request)
            response.raise_for_status()

            if not response.content:
                return {"status": "success"}

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
                message=f"RabbitMQ API returned an error ({e.response.status_code}): {e.response.text}",
                status_code=e.response.status_code,
            ) from e

    def get(self, path: str) -> dict:
        return self._request("GET", path)

    def post(self, path: str, payload: Optional[dict] = None):
        return self._request("POST", path, payload=payload)

    def put(self, path: str, payload: Optional[dict] = None):
        return self._request("PUT", path, payload=payload)

    def delete(self, path: str):
        return self._request("DELETE", path)
