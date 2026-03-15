from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
from .forms import SignupForm, SigninForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from .utils import send_activation_email
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        secret_key = request.POST.get("secret_key")
        print(request.POST.get("password"))
        print(request.POST.get("confirm_password"))

        if secret_key == settings.ATHENURA_SECRET_KEY:
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password"])
                user.save()

                uid64 = urlsafe_base64_encode(force_bytes(user.id))
                print("uid64:", uid64)
                token = default_token_generator.make_token(user)
                print("token:", token)
                activation_link = reverse("activate_account", kwargs={"uid64": uid64, "token": token})
                activation_url = f"{settings.DOMAIN_NAME}{activation_link}"
                send_activation_email(user, activation_url)
                print("activation_url: ",activation_url)
                messages.success(request, "Account created successfully! Please check your email to verify.")
                return redirect("signin_view")
        else:
            messages.error(request, "Secret key is not matched.")

    else:
        form = SignupForm()

    context = {
        "form" : form,
    }

    return render(request, "accounts/signup.html", context)

def activate_account(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(id=uid)

        if user.is_active:
            messages.warning(request, "This account has been already  activated.")
            return redirect("signin_view")
        
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account activated successfully. You can now login.")
            return redirect("signin_view")
        else:
            messages.error(request, "Activation link is invalid or expired.")
            return redirect("signin_view")
        
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, "Invalid activation link.")
        return redirect("signin_view")
    


def signin_view(request):
    if request.method == "POST":
        form = SigninForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    form.add_error(None, "Please verify your email first.")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = SigninForm()
    return render(request, "accounts/signin.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("signin_view")