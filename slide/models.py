import datetime
from django.db import models
from django.utils import timezone

class Slideshow(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=63, unique=True)
    date_published = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    source = models.TextField(verbose_name='Source code')
    options = models.JSONField(null=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)
