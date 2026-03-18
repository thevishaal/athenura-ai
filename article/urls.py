from django.urls import path
from . import views


urlpatterns = [
    path("article/", views.article, name="article"),
    path("generate-structure/", views.generate_structure, name="generate_structure"),
    path("generate-article/", views.generate_article,name="generate_article"),
]
