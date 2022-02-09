from django.contrib.contenttypes.models import ContentType
from graphene.types import String
from graphene_django import DjangoObjectType

from .models import Upload, User
from .node import Node


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username")


class UploadType(DjangoObjectType):

    presigned_url_get = String()
    presigned_url_put = String()

    class Meta:
        model = Upload
        interfaces = (Node,)
        convert_choices_to_enum = False


class ContentTypeType(DjangoObjectType):
    class Meta:
        model = ContentType
