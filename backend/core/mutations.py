from celery import current_app
from graphene import Field
from graphene.relay import ClientIDMutation

from .choices import UploadStatus
from .decorators import login_required
from .inputs import CreateUploadInput, IDInput
from .models import Upload
from .node import Node
from .types import UploadType


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
        upload = Upload.objects.get(**input)
        upload.status = UploadStatus.UPLOADED
        upload.save()
        current_app.send_task("backend.core.tasks.process_upload", (upload.id,))
        return FinishUpload(upload=upload)


class Mutations:
    create_upload = CreateUpload.Field()
    finish_upload = FinishUpload.Field()
    node = Node.Field()
