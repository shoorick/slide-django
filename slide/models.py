import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

'''
Slideshow
'''
class Slideshow(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=63, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_published = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    source = models.TextField(verbose_name='Source code', blank=True)
    options = models.JSONField(null=True, blank=True)
    stylesheet = models.TextField(verbose_name='CSS rules', blank=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

'''
User profile has one-to-one link to user
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=1024, blank=True)
    options = models.JSONField(null=True, blank=True)

    def __str__(self):
        return ' '.join((self.user.first_name, self.user.last_name))

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
