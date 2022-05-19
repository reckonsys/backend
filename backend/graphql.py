from graphene import ObjectType, Schema

from .core.mutations import Mutations as CoreMutations
from .core.queries import Queries as CoreQueries

from .questions.mutations import Mutations as BackendMutations
from .questions.queries import Queries as BackendQueries

# from .other.mutations import Mutations as OtherMutations
# from .other.queries import Queries as OtherQueries


class Query(
    CoreQueries,
    BackendQueries,
    # OtherQueries,
    # lastly,
    ObjectType,
):
    pass


class Mutation(
    CoreMutations,
    BackendMutations,
    # OtherMutations,
    # lastly,
    ObjectType,
):
    pass


schema = Schema(query=Query, mutation=Mutation)
