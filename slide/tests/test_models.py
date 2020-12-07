from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Profile, Slideshow

'''
Profile of user
'''
class ProfileModelTest(TestCase):
    def test_profile_has_str(self):
        self.assertIn('__str__', dir(Profile), msg='Profile has __str__')

'''
Slideshow
'''
class SlideshowModelTest(TestCase):
    def test_slideshow_has_str(self):
        self.assertIn('__str__', dir(Slideshow), msg='Slideshow has __str__')

'''
Fill models with data
'''
class FilledModelsTest(TestCase):

    def setUp(self):
        # make user without any name (default behavior for manage.py createsuperuser)
        # create profile implicitly
        User.objects.create_user(
            username='unnamed',
            email='unnamed@example.com',
            password='fake-password',
        )

        # make user with both names
        named_user = User.objects.create_user(
            username='named',
            email='named@example.com',
            password='fake-password',
            first_name='Name',
            last_name='Amen',
        )

        Slideshow.objects.create(
            name='First',
            slug='first',
            user=named_user,
            source='# First\n--\n## Slideshow\n\nwith Remark',
        )


    def test_profile_str_is_not_empty(self):
        for profile in Profile.objects.all():
            name = str(profile).strip();
            self.assertNotEqual(profile, '', msg='String representation of Profile is not empty')
