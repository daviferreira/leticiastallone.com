# coding: utf-8
from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    slug = models.SlugField(max_length=200, null=False, blank=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title
