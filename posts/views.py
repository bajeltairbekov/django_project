from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post




def main_view(reqesty):
    return render(reqesty,"base.html")


def hello_view(reqesty):
    return HttpResponse("hello world")


def html_view(reqesty):
    return render(reqesty,"base.html")


def posts_list_view(reqesty):
    posts = Post.objects.all()
    return render(reqesty, "posts/posts_list.html", context={"posts":posts})
# Create your views here.
