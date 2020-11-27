import datetime
from django.db import models
from django.utils import timezone

class Slideshow(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=63)
    date_published = models.DateTimeField('date published')
    is_published = models.BooleanField()
    source = models.TextField()
    # options = models.JSONField()

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)
