import hmac
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, Model
from django.db.models import PositiveSmallIntegerField as PSIF
from django.db.models import TextField, UUIDField

from .choices import UploadKind, UploadStatus, UserKind
from .storage import generate_presigned_url_get, generate_presigned_url_put


class BaseModel(Model):
    """
    TODO:
    In future, make use of DEFAULT_AUTO_FIELD = "django.db.models.UUIDAutoField"
    blocker: https://code.djangoproject.com/ticket/32577
    """

    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.id}"


class User(AbstractUser, BaseModel):
    kind = PSIF(choices=UserKind.choices, default=UserKind.CLIENT)

    def get_verify_token(self):
        result = hmac.new(
            settings.SECRET_KEY.encode("utf-8"), msg=str(self.id).encode("utf-8")
        )
        return result.hexdigest()

    def get_verification_link(self):
        return f"{settings.FRONTEND_PREFIX}/auth/verify/{self.id}/{self.get_verify_token()}"  # noqa: E501

    def validate_verify_token(self, digest):
        return hmac.compare_digest(digest, self.get_verify_token())

    def __str__(self):
        return f"{self.username}"


class Upload(BaseModel):
    error_message = TextField(null=True, blank=True)
    filename = CharField(max_length=250)
    kind = PSIF(choices=UploadKind.choices, default=UploadKind.PROFILE_PICTURE)
    mimetype = CharField(max_length=100)
    status = PSIF(choices=UploadStatus.choices, default=UploadStatus.UPLOADING)
    user = ForeignKey(User, on_delete=CASCADE, related_name="uploads")

    @property
    def key(self):
        """storage bucket key / object path"""
        return f"{settings.UPLOADS_PREFIX}/{self.kind}/{self.id}"

    def __str__(self):
        return f"[{self.user}] {self.filename}"

    @property
    def presigned_url_get(self):
        return generate_presigned_url_get(self.key)

    @property
    def presigned_url_put(self):
        return generate_presigned_url_put(self.key)
