from django.contrib import admin
from .models import ItemMenu


class ItemMenuAdmin(admin.ModelAdmin):
    search_fields = ["label", "link"]

admin.site.register(ItemMenu, ItemMenuAdmin)
