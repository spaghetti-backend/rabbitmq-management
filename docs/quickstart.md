# QuickStart

### Асинхронное использование

```python
from rabbitmq_management import AsyncRMQManagementAPI

async def main():
    async with AsyncRMQManagementAPI("http://localhost:15672", "guest", "guest") as api:
        queues = await api.queues.list()
        print(queues)
```
