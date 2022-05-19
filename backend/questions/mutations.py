from graphene import Field, ID
from graphene.relay import ClientIDMutation

from backend.core.node import Node
from backend.core.decorators import login_required

from .inputs import AnswerInput, CommentInput, QuestionInput, VoteInput
from .models import Answer, Comment, Question, Vote
from .types import AnswerType, CommentType, QuestionType, VoteType


class CreateAnswer(ClientIDMutation):
    answer = Field(AnswerType)
    Input = AnswerInput

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        input["question_id"] = Node.gid2id(input["question_id"])
        answer = Answer.objects.create(user=info.context.user, **input)
        return CreateAnswer(answer=answer)


class UpdateAnswer(ClientIDMutation):
    answer = Field(AnswerType)

    class Input(AnswerInput):
        id = ID(required=True)

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        id = input.get("id")
        Answer.objects.filter(id=id).update(**input)
        answer = Answer.objects.get(id=id)
        return UpdateAnswer(answer=answer)


class CreateComment(ClientIDMutation):
    comment = Field(CommentType)
    Input = CommentInput

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        input["object_id"] = Node.gid2id(input["object_id"])
        comment = Comment.objects.create(user=info.context.user, **input)
        return CreateComment(comment=comment)


class UpdateComment(ClientIDMutation):
    comment = Field(CommentType)

    class Input(CommentInput):
        id = ID(required=True)

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        id = input.get("id")
        Comment.objects.filter(id=id).update(**input)
        comment = Comment.objects.get(id=id)
        return UpdateComment(comment=comment)


class CreateQuestion(ClientIDMutation):
    question = Field(QuestionType)
    Input = QuestionInput

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        question = Question.objects.create(user=info.context.user, **input)
        return CreateQuestion(question=question)


class UpdateQuestion(ClientIDMutation):
    question = Field(QuestionType)

    class Input(QuestionInput):
        id = ID(required=True)

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        id = input.get("id")
        Question.objects.filter(id=id).update(**input)
        question = Question.objects.get(id=id)
        return UpdateQuestion(question=question)


class ApplyVote(ClientIDMutation):
    vote = Field(VoteType)
    Input = VoteInput

    @staticmethod
    @login_required
    def mutate_and_get_payload(root, info, **input):
        object_id = Node.gid2id(input.get("object_id"))
        content_type_id = input.get("content_type_id")
        kind = input.get("kind")
        filter = {
            "object_id": object_id,
            "content_type_id": content_type_id,
            "user": info.context.user,
        }
        if Vote.objects.filter(**filter).exists():
            Vote.objects.filter(**filter).update(kind=kind)
            vote = Vote.objects.filter(**filter).get()
        else:
            vote = Vote.objects.create(**filter, kind=kind)
        return ApplyVote(vote=vote)


class Mutations:
    apply_vote = ApplyVote.Field()
    create_answer = CreateAnswer.Field()
    create_comment = CreateComment.Field()
    create_question = CreateQuestion.Field()
    update_answer = UpdateAnswer.Field()
    update_comment = UpdateComment.Field()
    update_question = UpdateQuestion.Field()
