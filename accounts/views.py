from django.shortcuts import render

# Create your views here.
def signup_view(request):
    return render(request, "accounts/signup.html")


def signin_view(request):
    return render(request, "accounts/signin.html")