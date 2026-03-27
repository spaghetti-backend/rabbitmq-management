class RMQManagementError(Exception):
    """Base exception for the rabbitmq-management library."""


class RMQRequestError(RMQManagementError):
    """Exception raised when a request fails before reaching the RabbitMQ server."""


class RMQNetworkError(RMQRequestError):
    """Exception raised due to network issues (timeouts, connection drops, DNS failures)."""


class RMQApiError(RMQManagementError):
    """Exception raised when the RabbitMQ API returns an error response (HTTP 4xx or 5xx)."""

    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.status_code = status_code
