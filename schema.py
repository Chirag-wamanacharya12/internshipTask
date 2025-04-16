import graphene
from user.schema import Query as UserQuery

class Query(UserQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
