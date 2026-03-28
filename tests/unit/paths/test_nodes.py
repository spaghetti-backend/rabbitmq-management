import pytest

from rabbitmq_management.paths import BasePath, Paths


def test_all_nodes_endpoint():
    assert Paths.nodes.all() == BasePath.NODES


@pytest.mark.parametrize(
    "node, memory, binary, expected",
    [
        ("test@testmq", False, False, f"{BasePath.NODES}/test%40testmq"),
        ("test@testmq", True, False, f"{BasePath.NODES}/test%40testmq?memory=true"),
        ("test@testmq", False, True, f"{BasePath.NODES}/test%40testmq?binary=true"),
        (
            "test@testmq",
            True,
            True,
            f"{BasePath.NODES}/test%40testmq?memory=true&binary=true",
        ),
    ],
)
def test_node_detail_endpoints(node: str, memory: bool, binary: bool, expected: str):
    assert Paths.nodes.detail(node=node, memory=memory, binary=binary) == expected


def test_node_detail_should_raise_error_when_node_is_empty():
    with pytest.raises(ValueError, match="not be empty"):
        Paths.nodes.detail(node="")
