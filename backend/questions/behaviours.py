from django.db.models import Case, Count, F, IntegerField, When, QuerySet
from graphene import Int

from .choices import VoteKind


def vote_count(vote_kind):
    """CASE/WHEN statement to count up/down votes"""
    return Count(Case(When(votes__kind=vote_kind, then=1), output_field=IntegerField()))


class VotableQuerySet(QuerySet):
    def with_vote_count(self):
        return (
            self.annotate(vote_up=vote_count(VoteKind.UP))
            .annotate(vote_down=vote_count(VoteKind.DOWN))
            .annotate(vote_count=F("vote_up") - F("vote_down"))
        )


class VotableObjectType:
    vote_up = Int()
    vote_down = Int()
    vote_count = Int()


class CommentableQuerySet(VotableQuerySet):
    def with_comment_count(self):
        return self.annotate(comment_count=Count("comments"))


class CommentableObjectType(VotableObjectType):
    comment_count = Int()
