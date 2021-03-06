from django.db import models


class ItemMenu(models.Model):
    label = models.CharField(max_length=60)
    link = models.CharField(max_length=255)
    order = models.IntegerField(default=100000)

    def __unicode__(self):
        return "%s" % self.label
