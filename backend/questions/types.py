from graphene_django import DjangoObjectType

from backend.core.node import Node

from .behaviours import CommentableObjectType, VotableObjectType
from .models import Answer, Comment, Question, Vote


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (Node,)
        convert_choices_to_enum = False


class CommentType(VotableObjectType, DjangoObjectType):
    class Meta:
        model = Comment
        interfaces = (Node,)


class QuestionType(CommentableObjectType, DjangoObjectType):
    class Meta:
        model = Question
        interfaces = (Node,)


class AnswerType(CommentableObjectType, DjangoObjectType):
    class Meta:
        model = Answer
        interfaces = (Node,)
