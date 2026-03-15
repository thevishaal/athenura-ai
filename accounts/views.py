from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
from .forms import SignupForm, SigninForm, ChangePasswordForm, ForgotPasswordForm, ResetPasswordForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from .utils import send_activation_email, send_reset_email
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


# Create your views here.
@unauthenticated_user
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        secret_key = request.POST.get("secret_key")

        if secret_key == settings.ATHENURA_SECRET_KEY:
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password"])
                user.save()

                uid64 = urlsafe_base64_encode(force_bytes(user.id))
                token = default_token_generator.make_token(user)
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
    

@unauthenticated_user
def signin_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = SigninForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    redirect_to = request.POST.get('next') or next_url or 'dashboard'
                    return redirect(redirect_to)
                else:
                    form.add_error(None, "Please verify your email first.")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = SigninForm()
    return render(request, "accounts/signin.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("signin_view")

@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)

        if form.is_valid():

            user = request.user
            user.set_password(form.cleaned_data["new_password1"])
            user.save()

            update_session_auth_hash(request, user)

            messages.success(request, "Password changed successfully")
            return redirect("dashboard")

    else:
        form = ChangePasswordForm(request.user)

    return render(request, "accounts/change_password.html", {"form": form})


def forgot_password_view(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                uid64 = urlsafe_base64_encode(force_bytes(user.id))
                token = default_token_generator.make_token(user)
                reset_path = reverse("reset_password", kwargs={"uid64": uid64, "token": token})
                reset_link = f"{settings.DOMAIN_NAME}{reset_path}"
                print("reset link: ", reset_link)
                send_reset_email(user.email, reset_link)
                return render(request, "accounts/forgot_password_done.html")
            except User.DoesNotExist:
                form.add_error("email", "User with this email does not exist.")
    else:
        form = ForgotPasswordForm()
    return render(request, "accounts/forgot_password.html", {"form": form})



def reset_password_view(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is None or not default_token_generator.check_token(user, token):
        return render(request, "accounts/reset_password_invalid.html")

    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            
            messages.success(request, "Password reset is successfully!")

            return redirect("signin_view")
    else:
        form = ResetPasswordForm()

    return render(request, "accounts/reset_password.html", {"form": form})