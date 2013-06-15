from django.db import models


class ItemLink(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.URLField()
    order = models.IntegerField(default=100000)
    new_window = models.BooleanField(default=False)
    highlight = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % self.title
