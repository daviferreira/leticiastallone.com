from django.db import models

from content.models import Content


class Post(Content, models.Model):
    pass
