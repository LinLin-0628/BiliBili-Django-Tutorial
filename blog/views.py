from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "blog/index.html")


def blog_detail(request, blog_id):
    return render(request, "blog/blog_detail.html")


def create_blog(request):
    return render(request, "blog/create_blog.html")

