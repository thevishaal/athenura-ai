from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={
            "min_length": "Password must be at least 8 characters."
        },
        min_length=8
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={
            "required": "Please confirm your password."
        }
    )

    profile_img = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["full_name", "email", "profile_img"]

        widgets = {
            "full_name": forms.TextInput(),
            "email": forms.EmailInput()
        }

    # Email unique validation
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email

    # Password match validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                self.add_error("confirm_password", "Passwords do not match")

            try:
                validate_password(password)
            except forms.ValidationError as e:
                self.add_error("password", e)

        return cleaned_data
    
class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")

        if not self.user.check_password(old_password):
            raise forms.ValidationError("Old Password is incorrect.")

        return old_password
    
    def clean_new_password1(self):
        password = self.cleaned_data.get("new_password1")
        validate_password(password, self.user)
        return password
    
    def clean(self):
        cleaned_data = super().clean()

        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:

            if password != confirm_password:
                self.add_error("confirm_password", "Passwords do not match")

            try:
                validate_password(password)
            except forms.ValidationError as e:
                self.add_error("password", e)
        
        return cleaned_data
