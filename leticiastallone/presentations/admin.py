from django.contrib import admin
from content.admin import ContentAdmin
from .models import Presentation


class PresentationAdmin(ContentAdmin):
    pass

admin.site.register(Presentation, PresentationAdmin)
