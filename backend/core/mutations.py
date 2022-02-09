from celery import current_app
from graphene import Field
from graphene.relay import ClientIDMutation
from graphql_jwt.relay import ObtainJSONWebToken

from .choices import UploadStatus
from .decorators import login_required
from .inputs import CreateUploadInput, IDInput, RegisterInput, UpdateMeInput
from .models import Upload, User
from .node import Node
from .types import UploadType, UserType


class Register(ClientIDMutation):
    user = Field(UserType)
    Input = RegisterInput

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        username = input.get("username")
        password = input.get("password")
        email = f"{username}@backend.local"
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return Register(user=user)


class CreateUpload(ClientIDMutation):
    Input = CreateUploadInput
    upload = Field(UploadType)

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        upload = Upload.objects.create(user=info.context.user, **input)
        return CreateUpload(upload=upload)


class FinishUpload(ClientIDMutation):
    Input = IDInput
    upload = Field(UploadType)

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        upload = Upload.objects.get(id=Node.gid2id(input.get("id")))
        upload.status = UploadStatus.UPLOADED
        upload.save()
        current_app.send_task("backend.core.tasks.process_upload", (upload.id,))
        return FinishUpload(upload=upload)


class UpdateMe(ClientIDMutation):
    Input = UpdateMeInput
    me = Field(UserType)

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        User.objects.filter(id=info.context.user.id).update(**input)
        me = User.objects.get(id=info.context.user.id)
        return UpdateMe(me=me)


class Mutations:
    create_upload = CreateUpload.Field()
    finish_upload = FinishUpload.Field()
    login = ObtainJSONWebToken.Field()
    node = Node.Field()
    register = Register.Field()
    update_me = UpdateMe.Field()
