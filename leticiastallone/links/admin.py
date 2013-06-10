from django.contrib import admin
from .models import ItemLink


class ItemLinkAdmin(admin.ModelAdmin):
    search_fields = ["title", "description", "link"]

admin.site.register(ItemLink, ItemLinkAdmin)
