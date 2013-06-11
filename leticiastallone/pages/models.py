from django.db import models

from taggit.managers import TaggableManager

from content.models import Content


class Page(Content, models.Model):
    keywords = TaggableManager(blank=True)
