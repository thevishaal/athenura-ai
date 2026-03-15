from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={
            "required": "Password is required.",
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

        error_messages = {
            "full_name": {
                "required": "Full name is required."
            },
            "email": {
                "required": "Email address is required.",
                "invalid": "Enter a valid email address."
            }
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

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")

        return cleaned_data
    
class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)