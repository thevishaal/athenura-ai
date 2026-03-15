from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def social_media(request):
    return render(request, "social_media/social_media.html")