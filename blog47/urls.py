from django.contrib import admin
from django.urls import path
from posts.views import hello_view, html_view, posts_list_view, main_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_view),
    path("html/", html_view),
    path("posts/", posts_list_view),
    path("", main_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)