from django import forms


class CaptionForm(forms.Form):
    topic = forms.CharField(required=True)
    platform = forms.CharField(required=True)
    tone = forms.CharField(required=True)