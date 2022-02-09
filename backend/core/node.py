from graphene.relay import Node as _Node


class Node(_Node):
    class Meta:
        name = "Node"

    @staticmethod
    def to_global_id(type_, id):
        return str(id)
