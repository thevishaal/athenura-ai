from django.urls import path
from . import views


urlpatterns = [
    path("article-generater/", views.article, name="article"),
]
