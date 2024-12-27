from django.contrib import admin
from posts.models import Post, Catigory, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'discription', 'rate', 'created_at', 'updated_at')
admin.site.register(Catigory)
admin.site.register(Tag)


# Register your models here.
