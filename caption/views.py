from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .caption_prompt import generate_caption_content
import json
from .forms import CaptionForm

@login_required
def caption(request):
    if request.method == "POST":
        form = CaptionForm(request.POST)
        # Grab current offset, default to 0
        offset = int(request.POST.get("offset", 0))

        if not form.is_valid():
            return render(request, "caption/partials/caption_results.html", {
                "data": {"captions": []},
                "offset": offset,
                "next_offset": offset
            })

        topic = form.cleaned_data.get("topic")
        platform = form.cleaned_data.get("platform")
        tone = form.cleaned_data.get("tone")

        content = generate_caption_content(topic, platform, tone)
        data = json.loads(content)
        
        # Calculate the new offset based on how many captions were generated
        captions_count = len(data.get("captions", []))
        next_offset = offset + captions_count

        context = {
            "data": data,
            "offset": offset,
            "next_offset": next_offset
        }

        # 👉 Generate More -> Return only cards (which includes the next button)
        if offset > 0:
            return render(request, "caption/partials/caption_cards.html", context)

        # 👉 First load -> Return the full results wrapper
        return render(request, "caption/partials/caption_results.html", context)

    return render(request, "caption/caption.html")