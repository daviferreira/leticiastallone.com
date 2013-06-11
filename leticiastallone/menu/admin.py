from django.contrib import admin
from .models import ItemMenu


class ItemMenuAdmin(admin.ModelAdmin):
    search_fields = ['label', 'link']
    list_display = ['label', 'link', 'order']

admin.site.register(ItemMenu, ItemMenuAdmin)
