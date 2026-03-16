from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .blog_prompts import generate_blog_content
import json


# Create your views here.
@login_required
def blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)

        if not form.is_valid():
            return render(request, "blog/partials/form.html", {"form": form})
        
        topic = form.cleaned_data["topic"]
        word_count = form.cleaned_data["word_count"]
        tone = form.cleaned_data["tone"]
        style = form.cleaned_data["style"]
        audience =  form.cleaned_data["audience"]
        external_thoughts = form.cleaned_data["external_thoughts"]

        content = generate_blog_content(topic, word_count, tone, style, audience, external_thoughts)

        data = json.loads(content)
        return render(
            request, 
            "blog/partials/blog_result.html", 
            {
                "data": data
            }
        )
    
    form = BlogForm()
    return render(request, "blog/blog.html", {"form": form})