from graphene import ID, Int, String


class VoteInput:
    object_id = ID(required=True)
    content_type_id = Int(required=True)
    kind = Int(required=True)


class CommentInput:
    object_id = ID(required=True)
    content_type_id = Int(required=True)
    text = String(required=True)


class QuestionInput:
    text = String(required=True)
    title = String(required=True)


class AnswerInput:
    question_id = ID(required=True)
    text = String(required=True)
