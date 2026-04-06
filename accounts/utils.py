import requests
import threading
from django.conf import settings
from django.template.loader import render_to_string


def _send_email(payload):
    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=5)

    if response.status_code not in [200, 201]:
        print("Email failed:", response.text)


def send_activation_email(user, activation_url):

    context = {
        "user": user,
        "activation_url": activation_url
    }

    html_message = render_to_string("accounts/activation_email.html", context)

    payload = {
        "sender": {
            "name": settings.SENDER_DOMAIN_NAME,
            "email": settings.DEFAULT_FROM_EMAIL
        },
        "to": [{"email": user.email}],
        "subject": "Verify Your Email",
        "htmlContent": html_message
    }

    threading.Thread(target=_send_email, args=(payload,), daemon=True).start()


def send_reset_email(recipient_email, reset_link):

    context = {
        "reset_link": reset_link
    }

    html_message = render_to_string("accounts/reset_email.html", context)

    payload = {
        "sender": {
            "name": settings.SENDER_DOMAIN_NAME,
            "email": settings.DEFAULT_FROM_EMAIL
        },
        "to": [{"email": recipient_email}],
        "subject": "Reset Your Password",
        "htmlContent": html_message
    }

    threading.Thread(target=_send_email, args=(payload,), daemon=True).start()