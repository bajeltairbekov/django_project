from django.shortcuts import render, HttpResponse, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def registe_view(reqesty):
    if reqesty.method == "GET":
        form = RegisterForm
        return render(reqesty, "user/register.html", context={'form': form})
    if reqesty.method == "POST":
        form = RegisterForm(reqesty.POST)
        if  not form.is_valid():
            return render(reqesty, "user/register.html", context={'form': form})
        elif form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create(username=username, password=password)
            return redirect("home")


def login_view(reqesty):
    if reqesty.method == "GET":
        form = LoginForm()
        return render(reqesty, "user/login.html", context={'form': form})
    if reqesty.method == "POST":
        form = LoginForm(reqesty.POST)
        if  not form.is_valid():
            return render(reqesty, "user/login.html", context={'form': form})
        elif form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        if user:
                login(reqesty, user)
                return redirect("home")
        if not user:
            form.add_error(None,'пароль неверный')
            return render(reqesty, "user/login.html", context={'form': form})



# Create your views here.
