from django.db import models

from taggit.managers import TaggableManager

from content.models import Content


class Post(Content, models.Model):
    intro = models.TextField()
    tags = TaggableManager(blank=True)
