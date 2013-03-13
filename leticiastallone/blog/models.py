from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    tags = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
