from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup_view, name="signup_view"),
    path("signin/", views.signin_view, name="signin_view"),
]
