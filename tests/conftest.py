from collections.abc import AsyncIterator, Iterator

import pytest
import pytest_asyncio
import respx
from respx import MockRouter

from rabbitmq_management.http_clients import AsyncHTTPClient, HTTPClient
from rabbitmq_management.management_api import AsyncRMQManagementAPI, RMQManagementAPI


@pytest.fixture(scope="session")
def api_url():
    return "http://localhost:1234"


@pytest.fixture(scope="session")
def api_mock(api_url: str) -> Iterator[MockRouter]:
    with respx.mock(
        base_url=f"{api_url}/api/",
        assert_all_called=True,
        assert_all_mocked=True,
    ) as mock:
        yield mock


@pytest_asyncio.fixture(scope="session")
async def async_http_client(api_url: str) -> AsyncIterator[AsyncHTTPClient]:
    async with AsyncHTTPClient(
        api_url=f"{api_url}/api/",
        username="guest",
        password="guest",
        timeout=1.0,
    ) as client:
        yield client


@pytest.fixture(scope="session")
def http_client(api_url: str) -> Iterator[HTTPClient]:
    with HTTPClient(
        api_url=f"{api_url}/api/",
        username="guest",
        password="guest",
    ) as client:
        yield client


@pytest_asyncio.fixture(scope="session")
async def async_management_api(api_url: str) -> AsyncIterator[AsyncRMQManagementAPI]:
    async with AsyncRMQManagementAPI(
        api_url=api_url,
        username="guest",
        password="guest",
        timeout=1.0,
    ) as api:
        yield api


@pytest.fixture(scope="session")
def management_api(api_url: str) -> Iterator[RMQManagementAPI]:
    with RMQManagementAPI(
        api_url=api_url,
        username="guest",
        password="guest",
        timeout=1.0,
    ) as api:
        yield api
