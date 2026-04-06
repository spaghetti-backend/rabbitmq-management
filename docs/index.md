# RMQ Management Client

An asynchronous and synchronous Python client for the RabbitMQ Management HTTP
API, providing a structured interface over its endpoints.

## Key Features

- Dual Interface: Provides both AsyncRMQManagementAPI and RMQManagementAPI.

- HTTP Backend: Built on top of httpx for high-performance requests.

- Compatibility: Designed for RabbitMQ 3.11+.

- Environment: Python 3.9+ with full type hinting.

## Installation

```bash
pip install rabbitmq-management
```

## Usage Examples

### Asynchronous Interface

The library supports asynchronous context managers for automatic session cleanup.

```python

from rabbitmq_management import AsyncRMQManagementAPI

async def main():
    async with AsyncRMQManagementAPI(...) as rmq:
        # Get cluster overview
        stats = await rmq.overview()

        # Access sub-resources (e.g., queues)
        queues = await rmq.queues.all()

        # Perform health checks
        status = await rmq.aliveness_test(vhost="/")

# client = AsyncRMQManagementAPI(...)
# await client.overview()
# await client.close()
```

### Synchronous Interface

Identical to the async version but uses blocking calls.

```python

from rabbitmq_management import RMQManagementAPI

with RMQManagementAPI(...) as rmq:
    nodes = rmq.nodes.all()
    print(nodes)
```

## API Structure

Methods are grouped into sub-resources corresponding to the RabbitMQ Management
API endpoints.
Each sub-resource is accessible as an attribute of the client instance.

| Resource | Description |
| :--- | :--- |
| `rmq.queues` | Create, delete, purge, and fetch messages. |
| `rmq.users` | Manage users, password hashes, and limits. |
| `rmq.vhosts` | Manage virtual hosts and their state. |
| `rmq.permissions` | Manage standard and topic permissions. |
| `rmq.policies` | Manage runtime and operator policies. |
| `rmq.nodes` | Monitor cluster nodes and memory usage. |
