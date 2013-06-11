from django.db import models

from content.models import Content


class Page(Content, models.Model):
    pass
