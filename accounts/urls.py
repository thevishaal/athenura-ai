from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup_view, name="signup_view"),
    path("activate/<str:uid64>/<str:token>/", views.activate_account, name="activate_account"),
    path("signin/", views.signin_view, name="signin_view"),
    path("logout/", views.logout_view, name="logout"),
    path("change-password/", views.change_password, name="change_password"),
    path("forgot-password/", views.forgot_password_view, name="forgot_password"),
    path("reset-password/<str:uid64>/<str:token>/", views.reset_password_view, name="reset_password"),
]
