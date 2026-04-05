from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class QueuesAPI(BaseAPI):
    """
    Managing RabbitMQ queues and their messages.
    """

    def all(
        self, *, enable_queue_totals: bool = False, disable_stats: bool = False
    ) -> list[dict]:
        """
        List all queues in the cluster.

        Args:
            enable_queue_totals: Return simplified set of fields.
            disable_stats: Reduce CPU/bandwidth footprint by omitting detailed stats.
        """
        return self._http_client.get(
            Paths.queues.all(
                enable_queue_totals=enable_queue_totals, disable_stats=disable_stats
            )
        )

    def by_vhost(self, vhost: str) -> list[dict]:
        """List all queues in a specific virtual host."""
        return self._http_client.get(Paths.queues.by_vhost(vhost=vhost))

    def detail(self, vhost: str, queue: str) -> dict:
        """Get details of a specific queue."""
        return self._http_client.get(Paths.queues.detail(vhost=vhost, queue=queue))

    def set(self, vhost: str, queue: str, value: dict) -> dict:
        """
        Create or update a queue.

        Args:
            value: Dict with optional keys: 'auto_delete', 'durable', 'arguments',
                'node'.
        """
        return self._http_client.put(
            Paths.queues.detail(vhost=vhost, queue=queue), payload=value
        )

    def delete(self, vhost: str, queue: str) -> dict:
        """Delete a specific queue."""
        return self._http_client.delete(Paths.queues.detail(vhost=vhost, queue=queue))

    def bindings(self, vhost: str, queue: str) -> list[dict]:
        """List all bindings for a specific queue."""
        return self._http_client.get(Paths.queues.bindings(vhost=vhost, queue=queue))

    def purge(self, vhost: str, queue: str) -> dict:
        """Remove all messages from the queue without deleting the queue itself."""
        return self._http_client.delete(Paths.queues.contents(vhost=vhost, queue=queue))

    def actions(self, vhost: str, queue: str, value: dict) -> dict:
        """
        Perform administrative actions on a queue.

        Args:
            value: Dict with 'action' (e.g., {"action": "sync"} or "cancel_sync").
        """
        return self._http_client.post(
            Paths.queues.actions(vhost=vhost, queue=queue), payload=value
        )

    def messages(self, vhost: str, queue: str, value: dict) -> list[dict]:
        """
        Fetch messages from a queue for diagnostic purposes.

        Args:
            value: Dict with 'count', 'ackmode' (e.g., 'ack_requeue_true'),
                   'encoding', and optional 'truncate'.

        Note:
            This is a management tool, not a high-performance messaging API.
        """
        return self._http_client.post(
            Paths.queues.messages(vhost=vhost, queue=queue), payload=value
        )
