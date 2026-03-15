import requests
import threading
from django.conf import settings


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

    payload = {
        "sender": {
            "name": settings.SENDER_DOMAIN_NAME,
            "email": settings.DEFAULT_FROM_EMAIL
        },
        "to": [{"email": user.email}],
        "subject": "Verify Your Email",
        "htmlContent": f"""
        <div style="font-family:sans-serif">
        <h2>Hello {user.full_name}</h2>
        <p>Please verify your email address.</p>

        <a href="{activation_url}" 
        style="background:#6366f1;color:white;padding:12px 25px;border-radius:6px;text-decoration:none;">
        Verify Email
        </a>

        <p>If you didn’t create this account, ignore this email.</p>
        </div>
        """
    }

    threading.Thread(target=_send_email, args=(payload,), daemon=True).start()


def send_reset_email(recipient_email, reset_link):

    payload = {
        "sender": {
            "name": settings.SENDER_DOMAIN_NAME,
            "email": settings.DEFAULT_FROM_EMAIL
        },
        "to": [{"email": recipient_email}],
        "subject": "Reset Your Password",
        "htmlContent": f"""
        <div style="font-family:sans-serif; line-height:1.5;">
            <h2>Password Reset Request</h2>
            <p>We received a request to reset your password. Click the button below:</p>

            <a href="{reset_link}" 
            style="background:#6366f1;color:white;padding:12px 25px;border-radius:6px;text-decoration:none;display:inline-block;">
            Reset Password
            </a>

            <p>If you didn't request this, please ignore this email.</p>
            <p>This link will expire in 24 hours.</p>
        </div>
        """
    }

    threading.Thread(target=_send_email, args=(payload,), daemon=True).start()