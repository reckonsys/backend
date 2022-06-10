from graphene import ID, Field, Int, List

from backend.core.decorators import login_required
from backend.core.node import Node

from .models import Comment, Question
from .types import CommentType, QuestionType


class Queries(object):
    comments = Field(
        List(CommentType),
        object_id=ID(required=True),
        content_type_id=Int(required=True),
    )
    question = Field(QuestionType, id=ID(required=True))
    questions = Field(List(QuestionType))

    @login_required
    def resolve_question(self, info, id):
        return Question.objects.with_vote_count().get(id=Node.gid2id(id))

    @login_required
    def resolve_questions(self, info):
        return Question.objects.with_comment_count().with_vote_count()

    @login_required
    def resolve_comments(self, info, object_id, content_type_id):
        object_id = Node.gid2id(object_id)
        return Comment.objects.filter(
            object_id=object_id, content_type_id=content_type_id
        ).with_vote_count()
