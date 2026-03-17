import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SocialMediaForm
from .services.post_generator import generate_social_media_content


@login_required
def social_media(request):

    if request.method == "POST":

        form = SocialMediaForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                "social_media/partials/form.html",
                {"form": form},
            )

        topic = form.cleaned_data["topic"]
        platform = form.cleaned_data["platform"]
        tone = form.cleaned_data["tone"]

        content = generate_social_media_content(
            topic=topic,
            platform=platform,
            tone=tone
        )

        data = json.loads(content)

        return render(
            request,
            "social_media/partials/ai_result.html",
            {
                "topic": topic,
                "platform": platform,
                "tone": tone,
                "data": data,
            },
        )

    form = SocialMediaForm()

    return render(
        request,
        "social_media/social_media.html",
        {"form": form},
    )