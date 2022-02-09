from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class UserKind(IntegerChoices):
    ADMIN = 1, _("Admin")
    CLIENT = 2, _("Client")


class UploadKind(IntegerChoices):
    PROFILE_PICTURE = 1, _("Profile Picture")
    EXCEL_REPORT = 2, _("Excel Report")
    RESUME = 3, _("Resume")


class UploadStatus(IntegerChoices):
    UPLOADING = 1, _("Uploading")
    UPLOADED = 2, _("Uploaded")
    PROCESSING = 3, _("Processing")
    PROCESSED = 4, _("Processed")
    ERROR = 5, _("Error")
