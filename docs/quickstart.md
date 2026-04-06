# Quick Start

This guide will help you get up and running with the rabbitmq-management client.

## Installation

```bash
pip install rabbitmq-management
```

## Basic Usage

The library provides two main entry points: **AsyncRMQManagementAPI** for
asynchronous code and **RMQManagementAPI** for synchronous scripts.

> All classes and methods are fully type-annotated, so your IDE will provide
autocompletion and type hints.

### Asynchronous Example (Recommended)

Using an asynchronous context manager ensures that the underlying
httpx.AsyncClient is closed properly.

```python
import asyncio
from rabbitmq_management import AsyncRMQManagementAPI

async def main():
    uri = "http://localhost:15672"
    async with AsyncRMQManagementAPI(uri, "guest", "guest") as api:

        # 1. Get cluster overview
        overview = await api.overview()
        print(overview["rabbitmq_version"])

        # 2. List all queues in a specific virtual host
        queues = await api.queues.by_vhost(vhost="/")
        for q in queues:
            print(q["name"])

        # 3. Create a new queue
        await api.queues.set(vhost="/", queue="test-queue", value={
            "durable": True,
            "auto_delete": False
        })

if __name__ == "__main__":
    asyncio.run(main())
```

### Synchronous Example

If you are writing a simple script or working in a non-async environment:

```python
from rabbitmq_management import RMQManagementAPI

def run():
    with RMQManagementAPI("http://localhost:15672", "guest", "guest") as api:
        # Create a new queue
        api.queues.set(vhost="/", queue="test-queue", value={
            "durable": True,
            "auto_delete": False
        })

if __name__ == "__main__":
    run()
```

### Working with Virtual Hosts and Permissions

A common task is setting up a new environment:

```python
async with AsyncRMQManagementAPI(uri, "admin", "secret") as api:
    # Create a vhost
    await api.vhosts.set(vhost="prod_vhost", value={"description": "Production"})

    # Create a user with tags
    await api.users.set(user="developer", value={
        "password": "password123",
        "tags": "management"
    })
```

> Using context managers ensures connections are closed automatically.
