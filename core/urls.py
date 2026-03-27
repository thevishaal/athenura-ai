from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("about/", views.about, name="about"),
    path("policy/",views.policy, name="policy"),
    path("terms/",views.terms, name="terms"),
    path("contact/",views.contact, name="contact")
    
]
