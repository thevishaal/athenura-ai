from django.urls import path
from . import views


urlpatterns = [
    path("caption-Ai/", views.caption, name="caption"),
]
