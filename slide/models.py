import datetime
import markdown
import re
import yaml
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

    def parse_cleaver_slides(self):
        slides  = []
        options = {}

        for number, slide in enumerate(self.source.split('\n--')):
            if number == 0:
                content = slide.lstrip().split('\n\n', 2)

                if re.search('^[^\n]+:', content[0]): # first line contains colon
                    options = yaml.load(content.pop(-1))

                if ''.join(content).strip() != '': # non empty/whitespace
                    slides.append({'content': '\n\n'.join(content)}) # use content as slide
            else:
                lines = slide.split('\n', 1)
                slides.append({
                    'classes': lines[0].strip,
                    'content': lines[1],
                })

        for slide in slides: slide['content'] = markdown.markdown(slide['content'])

        return slides, options


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
