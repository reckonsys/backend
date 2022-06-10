from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import CASCADE, CharField, ForeignKey
from django.db.models import PositiveSmallIntegerField as PSIF
from django.db.models import TextField, UUIDField

from backend.core.models import BaseModel, User

from .behaviours import CommentableQuerySet, VotableQuerySet
from .choices import VoteKind


class Vote(BaseModel):
    object_id = UUIDField()
    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    kind = PSIF(choices=VoteKind.choices, default=VoteKind.UP)
    user = ForeignKey(User, on_delete=CASCADE, related_name="votes")

    class Meta:
        unique_together = ("object_id", "content_type", "user")

    def __str__(self):
        return f"[{self.content_object}] {self.user}: {self.get_kind_display()}"


class Comment(BaseModel):
    object_id = UUIDField()
    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    text = TextField(max_length=3000)
    user = ForeignKey(User, on_delete=CASCADE, related_name="comments")
    votes = GenericRelation(Vote, related_query_name="comment")

    objects = VotableQuerySet.as_manager()

    def __str__(self):
        return f"[{self.content_object}] {self.user}: {self.text}"


class Question(BaseModel):
    text = TextField(max_length=3000)
    title = CharField(max_length=200, unique=True)
    user = ForeignKey(User, on_delete=CASCADE, related_name="questions")
    comments = GenericRelation(Comment, related_query_name="question")
    votes = GenericRelation(Vote, related_query_name="question")

    objects = CommentableQuerySet.as_manager()

    def __str__(self):
        return f"[{self.user}] {self.title}"


class Answer(BaseModel):
    question = ForeignKey(Question, on_delete=CASCADE, related_name="answers")
    text = TextField(max_length=3000)
    user = ForeignKey(User, on_delete=CASCADE, related_name="answers")
    comments = GenericRelation(Comment, related_query_name="answer")
    votes = GenericRelation(Vote, related_query_name="answer")

    objects = CommentableQuerySet.as_manager()

    class Meta:
        unique_together = ("question", "user")

    def __str__(self):
        return f"[{self.user}] {self.text}"
