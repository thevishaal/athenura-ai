from django.shortcuts import render

# Create your views here.
def social_media(request):
    return render(request, "social_media/social_media.html")