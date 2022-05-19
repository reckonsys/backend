from django.contrib import admin

from .models import Answer, Comment, Question, Vote

admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Vote)
