from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup_view, name="signup_view"),
    path("activate/<str:uid64>/<str:token>/", views.activate_account, name="activate_account"),
    path("signin/", views.signin_view, name="signin_view"),
    path("logout/", views.logout_view, name="logout")
]
