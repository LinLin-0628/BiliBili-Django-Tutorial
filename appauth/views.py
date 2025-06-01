from django.http import JsonResponse
from django.shortcuts import render
import string
import random
from django.core.mail import send_mail
from .models import CaptchaModel


# Create your views here.
def login(request):
    return render(request, "blog/login.html")

def register(request):
    return render(request, "blog/register.html")

def send_email_captcha(request):
    email = request.GET.get("email")

    if not email:
        return JsonResponse({
            "code": 400,
            "message": "Must provide email address"
        }, status=400)

    # Generate random number as verification code
    captcha = "".join(random.sample(string.digits, 4))

    CaptchaModel.objects.update_or_create(email=email, defaults={"captcha": captcha})

    send_mail(
        subject = "Verification Code for Webpage",
        message = f"Your verification code is {captcha}",
        recipient_list=[email],
        from_email = None
    )


    return JsonResponse({
        "code": 200,
        "message": "Email sent"
    }, status=200)