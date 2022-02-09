from django.contrib.contenttypes.models import ContentType
from graphene import ID, Field, List
from graphene_django.debug import DjangoDebug

from .decorators import login_required
from .models import Upload
from .node import Node
from .types import ContentTypeType, UploadType, UserType


class Queries(object):
    node = Node.Field()
    content_types = Field(List(ContentTypeType))
    debug = Field(DjangoDebug, name="_debug")
    me = Field(UserType)
    upload = Field(UploadType, id=ID(required=True))
    uploads = Field(List(UploadType))

    def resolve_content_types(self, info):
        return ContentType.objects.all()

    @login_required
    def resolve_upload(self, info, id):
        return Upload.objects.get(id=id)

    @login_required
    def resolve_uploads(self, info):
        return Upload.objects.filter(user=info.context.user)

    @login_required
    def resolve_me(self, info):
        return info.context.user
