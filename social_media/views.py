import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.post_generator import generate_social_media_content
from django.contrib.auth.decorators import login_required


@csrf_exempt

@login_required
def social_media(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)

        topic = data.get("topic")
        platform = data.get("platform")
        tone = data.get("tone")

        if not topic or not platform or not tone:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        try:
            content = generate_social_media_content(topic, platform, tone)
            ideas_json = json.loads(content)
            return JsonResponse(ideas_json)
        except json.JSONDecodeError:
            return JsonResponse({"error": "AI response parsing failed"}, status=500)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "GET":
        return render(request, "social_media/social_media.html")

    return JsonResponse({"error": "Method not allowed"}, status=405)