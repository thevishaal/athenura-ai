from django import forms

class SocialMediaForm(forms.Form):
    topic = forms.CharField(required=True)
    platform = forms.CharField(required=True)
    tone = forms.CharField(required=True)