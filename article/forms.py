from django import forms


class ArticleStructureForm(forms.Form):
    topic = forms.CharField(required=True)
    tone = forms.CharField(required=True)
    length = forms.CharField(required=True)
    audience = forms.CharField(required=True)