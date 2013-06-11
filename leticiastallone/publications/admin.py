from django.contrib import admin
from content.admin import ContentAdmin
from .models import Article


class ArticleAdmin(ContentAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
