from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from groq import Groq
from .article_prompts import generate_article_structure, generate_full_article
from .forms import ArticleStructureForm
import json


@login_required
def article(request):
    form = ArticleStructureForm()
    return render(request, "article/article.html", {"form": form})


@login_required
@require_POST
def generate_structure(request):
    form = ArticleStructureForm(request.POST)


    if not form.is_valid():
        return render(request, "article/partials/form.html", {
            "form": form
        })

    topic = form.cleaned_data["topic"]
    tone = form.cleaned_data["tone"]
    length = form.cleaned_data["length"]
    audience = form.cleaned_data["audience"]

    try:
        ai_response = generate_article_structure(
            topic=topic,
            tone=tone,
            length=length,
            audience=audience
        )

        data = json.loads(ai_response)

    except json.JSONDecodeError:
        return render(request, "article/partials/error.html", {
            "error": "AI returned invalid JSON. Try again."
        })

    except Exception as e:
        return render(request, "article/partials/error.html", {
            "error": f"Something went wrong: {str(e)}"
        })

    return render(
        request,
        "article/partials/article_structure.html",
        {
            "data": data,
            "tone": tone,
            "length": length,
            "audience": audience
        }
    )


@login_required
@require_POST
def generate_article(request):
    title = request.POST.get("title")
    structure = request.POST.get("structure")
    tone = request.POST.get("tone")
    length = request.POST.get("length")
    audience = request.POST.get("audience")

    if not title or not structure:
        return render(request, "article/partials/error.html", {
            "error": "Missing required data. Please regenerate structure."
        })


    ai_response = generate_full_article(
        title=title,
        structure=structure,
        tone=tone,
        length=length,
        audience=audience
    )

    data = json.loads(ai_response)

    return render(
        request,
        "article/partials/full_article.html",
        {
            "article": data
        }
    )