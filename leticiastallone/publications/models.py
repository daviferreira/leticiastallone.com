from django.conf import settings
from django.db import models

from content.models import Content


class Article(Content, models.Model):
    authors = models.TextField()
    journal = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
