from urllib.parse import quote


def prepare_name(name: str, field_name: str, /) -> str:
    if not name or not isinstance(name, str):
        raise ValueError(f"{field_name} should not be empty and must be a string")

    return quote(name, safe="")


def prepare_vhost(vhost: str, /) -> str:
    return prepare_name(vhost, "VHost")


def prepare_node(node: str, /) -> str:
    return prepare_name(node, "Node")


def prepare_connection(connection: str, /) -> str:
    return prepare_name(connection, "Connection")


def prepare_exchange(exchange: str, /) -> str:
    return prepare_name(exchange, "Exchange")


def prepare_username(username: str, /) -> str:
    return prepare_name(username, "Username")


def prepare_queue(queue: str, /) -> str:
    return prepare_name(queue, "Queue")


def prepare_channel(channel: str, /) -> str:
    return prepare_name(channel, "Channel")


def prepare_consumer(consumer: str, /) -> str:
    return prepare_name(consumer, "Consumer")


def prepare_component(component: str, /) -> str:
    return prepare_name(component, "Component")


def prepare_parameter(parameter: str, /) -> str:
    return prepare_name(parameter, "Parameter")
