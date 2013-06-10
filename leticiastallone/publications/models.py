from django.conf import settings
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    authors = models.TextField()
    journal = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to=settings.MEDIA_ROOT)
    keywords = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
