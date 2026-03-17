from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .caption_prompt import generate_caption_content
import json
from .forms import CaptionForm


# Create your views here.
@login_required
def caption(request):
    if request.method == "POST":
        form = CaptionForm(request.POST)

        if not form.is_valid():
            return render(request, "caption/partials/form.html", {"form": form})
        
        topic = form.cleaned_data.get("topic")
        platform = form.cleaned_data.get("platform")
        tone = form.cleaned_data.get("tone")

        content = generate_caption_content(topic, platform, tone)
        data = json.loads(content)

        return render(
            request,
            "caption/partials/caption_result.html",
            {
                "form": form,
                "data": data
            }
        )

    form = CaptionForm()

    if request.headers.get("HX-Request"):
        return render(request, "caption/partials/form.html", {"form": form})

    return render(request, "caption/caption.html", {"form": form})