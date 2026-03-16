from django import forms


class BlogForm(forms.Form):
    topic = forms.CharField(required=True)
    word_count = forms.CharField(required=True)
    tone = forms.CharField(required=True)
    style = forms.CharField(required=True)
    audience =  forms.CharField(required=True)
    external_thoughts = forms.CharField(required=False, widget=forms.Textarea)