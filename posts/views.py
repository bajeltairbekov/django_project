from django.shortcuts import render
from django.http import HttpResponse




def hello_view(reqesty):
    return HttpResponse("hello world")


def html_view(reqesty):
    return render(reqesty,"base.html")
# Create your views here.
