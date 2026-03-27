import pytest
import pytest_asyncio
from collections.abc import AsyncIterator, Iterator
from rabbitmq_management._http_clients import AsyncHTTPClient, HTTPClient


@pytest.fixture
def api_url():
    return "http://localhost:1234"


@pytest_asyncio.fixture
async def async_http_client(api_url: str) -> AsyncIterator[AsyncHTTPClient]:
    async with AsyncHTTPClient(
        api_url=api_url,
        username="guest",
        password="guest",
        timeout=1.0,
    ) as client:
        yield client


@pytest.fixture
def http_client(api_url: str) -> Iterator[HTTPClient]:
    with HTTPClient(
        api_url=api_url,
        username="guest",
        password="guest",
    ) as client:
        yield client
