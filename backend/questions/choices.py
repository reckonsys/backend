from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class VoteKind(IntegerChoices):
    UP = 1, _("Up")
    DOWN = 2, _("Down")
