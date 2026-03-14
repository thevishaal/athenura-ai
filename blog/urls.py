from django.urls import path
from . import views


urlpatterns = [
    path("blog-generator/", views.blog, name="blog"),
]
