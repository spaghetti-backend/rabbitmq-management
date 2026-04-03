from rabbitmq_management.paths import Paths

from .base_api import BaseAPI


class QueuesAPI(BaseAPI):
    def all(
        self, *, enable_queue_totals: bool = False, disable_stats: bool = False
    ) -> list[dict]:
        """
        A list of all queues.
        The parameter 'enable_queue_totals=True' can be used in combination
        with the 'disable_stats=True' parameter to return a reduced set of fields and
        significantly reduce the amount of data returned by this endpoint.
        That in turn can significantly reduce CPU and bandwidth footprint of such requests.
        """
        return self._http_client.get(
            Paths.queues.all(
                enable_queue_totals=enable_queue_totals, disable_stats=disable_stats
            )
        )

    def by_vhost(self, vhost: str) -> list[dict]:
        """
        A list of all queues in a given virtual host.
        """
        return self._http_client.get(Paths.queues.by_vhost(vhost=vhost))

    def detail(self, vhost: str, queue: str) -> dict:
        """
        An individual queue.
        """
        return self._http_client.get(Paths.queues.detail(vhost=vhost, queue=queue))

    def set(self, vhost: str, queue: str, value: dict) -> dict:
        """
        To set a queue, you will need a body looking something like this:

        {
          "auto_delete": False,
          "durable": True,
          "arguments": {},
          "node": "test@rabbitmq"
        }

        All keys are optional.
        """
        return self._http_client.put(
            Paths.queues.detail(vhost=vhost, queue=queue), payload=value
        )

    def delete(self, vhost: str, queue: str) -> dict:
        """
        Delete the queues.
        """
        return self._http_client.delete(Paths.queues.detail(vhost=vhost, queue=queue))

    def bindings(self, vhost: str, queue: str) -> list[dict]:
        """
        A list of all bindings on a given queue.
        """
        return self._http_client.get(Paths.queues.bindings(vhost=vhost, queue=queue))

    def purge(self, vhost: str, queue: str) -> dict:
        """
        Delete all messages from a queue.
        """
        return self._http_client.delete(Paths.queues.contents(vhost=vhost, queue=queue))

    def actions(self, vhost: str, queue: str, value: dict) -> dict:
        """
        Actions that can be taken on a queue. Set a 'value' like:

        {"action":"sync"}

        Currently the actions which are supported are sync and cancel_sync.
        """
        return self._http_client.post(
            Paths.queues.actions(vhost=vhost, queue=queue), payload=value
        )

    def messages(self, vhost: str, queue: str, value: dict) -> list[dict]:
        """
        Get messages from a queue. You should set a 'value' looking like:

        {
          "count": 5,
          "ackmode": "ack_requeue_true",
          "encoding": "auto",
          "truncate": 50000
        }

        'count' controls the maximum number of messages to get.
        You may get fewer messages than this if the queue cannot immediately provide them.

        'ackmode' determines whether the messages will be removed from the queue.
        if ackmode is ack_requeue_true or reject_requeue_true they will be requeued
        if ackmode is ack_requeue_false or reject_requeue_false they will be removed.

        'encoding' must be either "auto"
        (in which case the payload will be returned as a string if it is valid UTF-8,
        and base64 encoded otherwise),
        or "base64" (in which case the payload will always be base64 encoded).

        If 'truncate' is present it will truncate the message payload if it is larger than
        the size given (in bytes).

        truncate is optional; all other keys are mandatory.

        Please note that the get path in the HTTP API is intended for diagnostics etc
        it does not implement reliable delivery and so should be treated as
        a sysadmin's tool rather than a general API for messaging.
        """
        return self._http_client.post(
            Paths.queues.messages(vhost=vhost, queue=queue), payload=value
        )
