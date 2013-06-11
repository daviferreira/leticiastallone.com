from django.contrib import admin
from content.admin import ContentAdmin
from .models import Post


class PostAdmin(ContentAdmin):
    pass

admin.site.register(Post, PostAdmin)
