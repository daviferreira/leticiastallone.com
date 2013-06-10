from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager


class Article(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    authors = models.TextField()
    journal = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    keywords = TaggableManager(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
