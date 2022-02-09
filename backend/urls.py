from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path("health_check", lambda _: HttpResponse("ok")),
    path("admin/", admin.site.urls),
]
