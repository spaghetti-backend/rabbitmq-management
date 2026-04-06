# RMQ Management Client

An asynchronous and synchronous Python client for the RabbitMQ Management HTTP API.

## Key Features

- **Dual Interface**: Provides both AsyncRMQManagementAPI and RMQManagementAPI.

- **HTTP Backend**: Built on top of httpx for high-performance requests.

- **Compatibility**: Designed for RabbitMQ 3.11+.

- **Environment**: Python 3.9+ with full type hinting.

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
    # Using as a context manager
    async with AsyncRMQManagementAPI("http://localhost:15672", "guest", "guest") as rmq:
        # Get cluster overview
        stats = await rmq.overview()

        # Access sub-resources (e.g., queues)
        queues = await rmq.queues.all()

        # Perform health checks
        status = await rmq.aliveness_test(vhost="/")

# Manual session management:
# client = AsyncRMQManagementAPI(...)
# await client.overview()
# await client.close()
```

### Synchronous Interface

Identical to the async version but uses blocking calls.

```python

from rabbitmq_management import RMQManagementAPI

with RMQManagementAPI("http://localhost:15672", "guest", "guest") as rmq:
    nodes = rmq.nodes.all()
    print(nodes)
```

## API Structure

Methods are grouped into sub-resources matching the RabbitMQ Management API endpoints:

| Resource | Description |
| :--- | :--- |
| `rmq.queues` | Creating, deleting, purging, and fetching messages. |
| `rmq.users` | Managing users, password hashes, and user limits. |
| `rmq.vhosts` | Managing virtual hosts and their operational state. |
| `rmq.permissions` | Standard and Topic Permissions management. |
| `rmq.policies` | Managing runtime and operator policies. |
| `rmq.nodes` | Monitoring cluster nodes and memory statistics. |

Full API reference and detailed method parameters are available in the [documentation](https://rabbitmq-management.readthedocs.io/en/latest/).

## Roadmap

- [ ] Full API coverage for the latest RabbitMQ Management specifications
- [ ] Resource-oriented model (Queue, User, VHost objects)
- [ ] Expanded test suite for cluster configurations
- [ ] Optional HTTP backends via extras (requests, aiohttp)
