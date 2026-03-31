from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "core/dashboard.html")

def about(request):
    return render(request, 'core/about.html')

def policy(request):
    return render(request, 'core/policy.html')

def terms(request):
    return render(request,'core/terms.html')

def contact(request):
    return render(request,'core/contact.html')