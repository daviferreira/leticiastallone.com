from django.db import models


class ItemMenu(models.Model):
    label = models.CharField(max_length=60)
    link = models.URLField()
    order = models.IntegerField(default=100000)

    def __unicode__(self):
        return "%s <%s>" % (self.label, self.link)
