# coding: utf-8
from datetime import datetime

from django.db import models

from taggit.managers import TaggableManager


class Content(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    abstract = models.TextField()
    body = models.TextField(blank=False, null=False)
    slug = models.SlugField(max_length=200, null=False, blank=False)
    pub_date = models.DateTimeField(blank=False, null=False, default=datetime.now())
    is_published = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title
