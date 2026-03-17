from django.urls import path
from . import views


urlpatterns = [
    path("article/", views.article, name="article"),
]
