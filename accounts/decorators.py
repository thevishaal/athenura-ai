from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in.")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
        