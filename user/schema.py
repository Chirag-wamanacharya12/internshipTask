import graphene
from graphene_django.types import DjangoObjectType
from .models import User  # Make sure this points to your custom User model

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")  # Ensure these fields exist

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(root, info):
        return User.objects.all()

schema = graphene.Schema(query=Query)
