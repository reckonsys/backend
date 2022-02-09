from graphene import ObjectType, Schema

from .core.mutations import Mutations as CoreMutations
from .core.queries import Queries as CoreQueries

# from .other.mutations import Mutations as OtherMutations
# from .other.queries import Queries as OtherQueries


class Query(
    CoreQueries,
    # OtherQueries,
    # lastly,
    ObjectType,
):
    pass


class Mutation(
    CoreMutations,
    # OtherMutations,
    # lastly,
    ObjectType,
):
    pass


schema = Schema(query=Query, mutation=Mutation)
