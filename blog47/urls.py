from django.contrib import admin
from django.urls import path
from posts.views import hello_view, html_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_view),
    path("html/", html_view)
]
