from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    keywords = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
