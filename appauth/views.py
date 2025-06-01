from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
import string
import random
from django.core.mail import send_mail
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login(request):
    return render(request, "blog/login.html")

@require_http_methods(["GET", "POST"])
def register(request):

    if request.method == "GET":
        return render(request, "blog/register.html")
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            User.objects.create_user(email=email, username=username, password=password)


            return redirect(reverse("appauth:login"))

        else:
            print(form.errors)
            return redirect(reverse("appauth:register"))

            # return render(request, "blog/register.html", {"form": form})



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