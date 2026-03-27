from typing import Optional

import pytest

from rabbitmq_management._paths import BasePath, Paths


@pytest.mark.parametrize(
    "vhost, enable_queue_totals, disable_stats, expected",
    [
        (None, False, False, BasePath.QUEUES),
        (None, True, False, f"{BasePath.QUEUES}?enable_queue_totals=true"),
        (None, False, True, f"{BasePath.QUEUES}?disable_stats=true"),
        (
            None,
            True,
            True,
            f"{BasePath.QUEUES}?enable_queue_totals=true&disable_stats=true",
        ),
        ("test\\vhost", True, True, f"{BasePath.QUEUES}/test%5Cvhost"),
    ],
)
def test_queues_endpoints(
    vhost: Optional[str], enable_queue_totals: bool, disable_stats: bool, expected: str
):
    assert (
        Paths.queues(
            vhost=vhost,
            enable_queue_totals=enable_queue_totals,
            disable_stats=disable_stats,
        )
        == expected
    )


def test_queues_should_raises_error_when_vhost_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.queues(vhost="")


@pytest.mark.parametrize(
    "vhost, queue, if_empty, if_unused, expected",
    [
        (
            "test\\vhost",
            "test\\queue",
            False,
            False,
            f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue",
        ),
        (
            "test\\vhost",
            "test\\queue",
            True,
            False,
            f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue?if-empty=true",
        ),
        (
            "test\\vhost",
            "test\\queue",
            False,
            True,
            f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue?if-unused=true",
        ),
        (
            "test\\vhost",
            "test\\queue",
            True,
            True,
            f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue?if-empty=true&if-unused=true",
        ),
    ],
)
def test_queue_detail_endpoints(
    vhost: str, queue: str, if_empty: bool, if_unused: bool, expected: str
):
    assert (
        Paths.queues.detail(vhost, queue, if_empty=if_empty, if_unused=if_unused)
        == expected
    )


@pytest.mark.parametrize(
    "vhost, queue",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_queue_detail_should_raises_error_when_name_is_empty(vhost: str, queue: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.queues.detail(vhost, queue)


def test_queue_bindings_endpoint():
    assert (
        Paths.queues.bindings("test\\vhost", "test\\queue")
        == f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue/bindings"
    )


@pytest.mark.parametrize(
    "vhost, queue",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_queue_bindings_should_raises_error_when_name_is_empty(vhost: str, queue: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.queues.bindings(vhost, queue)


def test_queue_contents_endpoint():
    assert (
        Paths.queues.contents("test\\vhost", "test\\queue")
        == f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue/contents"
    )


@pytest.mark.parametrize(
    "vhost, queue",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_queue_contents_should_raises_error_when_name_is_empty(vhost: str, queue: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.queues.contents(vhost, queue)


def test_queue_actions_endpoint():
    assert (
        Paths.queues.actions("test\\vhost", "test\\queue")
        == f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue/actions"
    )


@pytest.mark.parametrize(
    "vhost, queue",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_queue_actions_should_raises_error_when_name_is_empty(vhost: str, queue: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.queues.actions(vhost, queue)


def test_queue_messages_endpoint():
    assert (
        Paths.queues.messages("test\\vhost", "test\\queue")
        == f"{BasePath.QUEUES}/test%5Cvhost/test%5Cqueue/get"
    )


@pytest.mark.parametrize(
    "vhost, queue",
    [
        ("", "test"),
        ("test", ""),
    ],
)
def test_queue_messages_should_raises_error_when_name_is_empty(vhost: str, queue: str):
    with pytest.raises(ValueError, match="not be empty"):
        Paths.queues.messages(vhost, queue)
