import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.post_generator import generate_social_media_content


@csrf_exempt
def social_media(request):

    if request.method == "POST":

        data = json.loads(request.body)

        topic = data.get("topic")
        platform = data.get("platform")
        tone = data.get("tone")

        if not topic or not platform or not tone:
            return JsonResponse({"error":"Missing required fields"}, status=400)

        content = generate_social_media_content(topic, platform, tone)

        # print(topic, platform, tone)
        try:
            ideas_json = json.loads(content)
        except:
            return JsonResponse({"error":"AI response parsing failed"}, status=500)


        return JsonResponse(ideas_json)
    
    elif request.method == "GET":
        return render(request, "social_media/social_media.html")

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    