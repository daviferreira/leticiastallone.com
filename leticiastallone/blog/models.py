from django.db import models

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=60)
    intro = models.TextField()
    body = models.TextField()
    tags = TaggableManager(blank=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
