from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Profile, Slideshow

'''
Profile of user
'''
class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # make user without any name (default behavior for manage.py createsuperuser)
        # create profile implicitly
        User.objects.create_user({
            'username': 'unnamed',
            'email': 'unnamed@example.com',
            'password': 'fake-password',
        })

        # make user with both names
        User.objects.create_user({
            'username': 'named',
            'email': 'named@example.com',
            'password': 'fake-password',
            'first_name': 'Name',
            'last_name': 'Amen',
        })


    def test_profile_has_str(self):
        self.assertIn('__str__', dir(Profile), msg='Profile has __str__')

    def test_profile_str_is_not_empty(self):
        for profile in Profile.objects.all():
            name = str(profile).strip();
            self.assertNotEqual(profile, '', msg='String representation of Profile is not empty')

'''
Slideshow
'''
class SlideshowModelTest(TestCase):
    def test_slideshow_has_str(self):
        self.assertIn('__str__', dir(Slideshow), msg='Slideshow has __str__')
