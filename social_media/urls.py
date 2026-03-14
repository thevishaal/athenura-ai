from django.urls import path
from . import views


urlpatterns = [
    path("social-ideas/", views.social_media, name="social_media"),
]
