from django.db import models

from content.models import Content


class Presentation(Content, models.Model):
    embed = models.CharField(max_length=255)
