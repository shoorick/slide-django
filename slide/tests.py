from django.test import TestCase

from .models import Profile, Slideshow

class ProfileModelTest(TestCase):
    def test_profile_has_str(self):
        self.assertIn('__str__', dir(Profile), msg='Profile has __str__')

class SlideshowModelTest(TestCase):
    def test_slideshow_has_str(self):
        self.assertIn('__str__', dir(Slideshow), msg='Slideshow has __str__')
