# API Overview

The rabbitmq-management library is structured to mirror the RabbitMQ Management
HTTP API. The main entry point is either **AsyncRMQManagementAPI** or
**RMQManagementAPI**, which exposes specialized sub-resources as attributes.

## Main Entry Points

| Class | Description |
| :--- | :--- |
| `AsyncRMQManagementAPI` | **Recommended.** Asynchronous client based on `httpx.AsyncClient`. |
| `RMQManagementAPI` | Synchronous (blocking) client based on `httpx.Client`. |

## Sub-resources Reference

All sub-resources are exposed as attributes of the main API instance (e.g., `api.queues`).
Class names follow a consistent async/sync convention: synchronous variants use
the same names without the `Async` prefix (e.g., `AsyncQueuesAPI` → `QueuesAPI`).

### Core Infrastructure

#### nodes (AsyncNodesAPI)

- List cluster nodes, get individual node details, and monitor memory/binary usage.

#### vhosts (AsyncVHostsAPI)

- Create, delete, and manage virtual hosts.
- List connections and channels per vhost.

### Messaging Resources

#### queues (AsyncQueuesAPI)

- Full lifecycle: create, list, and delete queues.
- Operational tasks: purge messages, get messages (diagnostics), and manual sync.
- Retrieve bindings for a specific queue.

#### exchanges (AsyncExchangesAPI)

- Create, list, and delete exchanges, and retrieve their bindings.

### Access Control & Security

#### users (AsyncUsersAPI)

- Manage user credentials (passwords/hashes) and tags (administrator, monitoring).

#### permissions (AsyncPermissionsAPI)

- Manage standard AMQP permissions (configure, write, read regex).

### Configuration & Automation

#### policies (AsyncPoliciesAPI)

- Manage Runtime Policies (HA, TTL, etc.).
- Access to policies.operator for enforced limits that users cannot override.

#### definitions (AsyncDefinitionsAPI)

- Import and export the entire cluster configuration as a JSON file.

### Shared Methods

The main API classes (`AsyncRMQManagementAPI` / `RMQManagementAPI`) also provide
top-level methods for cluster-wide information:

- `overview()`: Returns statistics about the whole cluster (versions, message
rates, object totals).
- `aliveness_test(vhost)`: A lightweight check to verify the node is responsive.
- `health_check()`: Detailed health check of the target node.
- `close()`: Closes the underlying HTTP connection pool (called automatically
when using a context manager).

## Error Handling

All API calls raise custom exceptions to provide consistent error handling.
These can be imported directly from the root package.

Non-2xx responses raise `RMQApiError`.
Network-level failures (connection errors, timeouts) raise `RMQRequestError`.

Exceptions are not suppressed and must be handled by the caller.

### Exception Hierarchy

#### RMQManagementError

- The base class for all exceptions raised by this library.

#### RMQRequestError

- Raised for any issues related to the HTTP request process.
- `RMQNetworkError`: Specifically for connection failures, drops, or timeouts.

#### RMQApiError

- Raised when the RabbitMQ API returns an error response (HTTP 4xx or 5xx).
- `status_code`: The HTTP status code (e.g., 404, 401).
- `reason`: A dictionary with the parsed JSON error from RabbitMQ, or None.
- `text`: The raw response body.

### Example

```python
from rabbitmq_management import AsyncRMQManagementAPI, RMQApiError, RMQRequestError

try:
    async with AsyncRMQManagementAPI(uri, user, pwd) as api:
        await api.overview()
except RMQApiError as e:
    print(f"API returned {e.status_code}: {e.reason}")
except RMQRequestError as e:
    print(f"HTTP request failed: {e}")
```
