from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "core/dashboard.html")

def about(request):
    return render(request, 'about.html')

def policy(request):
    return render(request, 'policy.html')

def terms(request):
    return render(request,'terms.html')

def contact(request):
    return render(request,'contact.html')