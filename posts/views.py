from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm




def main_view(reqesty):
    if reqesty.method == "GET":
      return render(reqesty,"base.html")


def hello_view(reqesty):
    return HttpResponse("hello world")


def html_view(reqesty):
    return render(reqesty,"base.html")


def posts_list_view(reqesty):
    if reqesty.method == "GET":
        posts = Post.objects.all()
        return render(reqesty, "posts/posts_list.html", context={"posts":posts})


def post_detail_view(reqesty,id):
    if reqesty.method == "GET":
        post = Post.objects.get(id=id)
        return render(reqesty, 'posts/post_detail.html', context={'post': post})


def post_create_view(reqesty):
    if reqesty.method == "GET":
        form = PostForm()
        return render(reqesty, 'posts/post_create.html', context={"form":form})
    if reqesty.method=="POST":
        data = reqesty.POST
        image = reqesty.FILES.get("image")
        title = data.get("title")
        discription = data.get("discription")
        post = Post.objects.create(title=title,discription=discription,image=image)

        return redirect("/posts/")
# Create your views here.
