from django.contrib import admin
from content.admin import ContentAdmin
from .models import Page


class PageAdmin(ContentAdmin):
    pass

admin.site.register(Page, PageAdmin)
