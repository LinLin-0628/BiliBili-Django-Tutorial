from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.urls.base import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):

    return render(request, "blog/index.html")


def blog_detail(request, blog_id):
    return render(request, "blog/blog_detail.html")

@login_required(login_url=reverse_lazy("appauth:login"))
@require_http_methods(["GET", "POST"])
def create_blog(request):

    if request.method == "GET":
        categories = BlogCategory.objects.all()

        return render(request, "blog/create_blog.html", {
            "categories": categories,
        })

    else:
        form = CreateBlogForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            category_id = form.cleaned_data.get("category")

            category = BlogCategory.objects.get(id=category_id)

            blog = Blog.objects.create(
                title=title,
                content=content,
                category=category,
                author=request.user
            )

            return JsonResponse({
                "code": 200,
                "message": "successfully created blog",
                "data": {
                    "blog_id": blog.id
                }
            }, status=200)

        else:
            print(form.errors)
            return JsonResponse({
                "code": 400,
                "message": "form invalid",
            }, status=400)





