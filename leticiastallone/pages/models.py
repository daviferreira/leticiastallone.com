from django.db import models

from taggit.managers import TaggableManager


class Page(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    keywords = TaggableManager(blank=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
