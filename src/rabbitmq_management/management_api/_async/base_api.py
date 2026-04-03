from rabbitmq_management import http_clients


class BaseAPI:
    def __init__(self, http_client: http_clients.AsyncHTTPClient) -> None:
        self._http_client = http_client
