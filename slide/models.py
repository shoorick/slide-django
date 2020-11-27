from django.db import models

class Slideshow:
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=63)
    date_published = models.DateTimeField('date published')
    is_published = models.BooleanField()
    source = models.TextField()
    options = models.JSONField()

