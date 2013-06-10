from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Page, PageAdmin)
