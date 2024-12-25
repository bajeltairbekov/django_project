from django.contrib import admin
from django.urls import path
from posts.views import hello_view, html_view, posts_list_view, main_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_view),
    path("html/", html_view),
    path("posts/", posts_list_view),
    path("", main_view)
]
