from django.test import TestCase, Client

from .models import Profile, Slideshow

class ProfileModelTest(TestCase):
    def test_profile_has_str(self):
        self.assertIn('__str__', dir(Profile), msg='Profile has __str__')

class SlideshowModelTest(TestCase):
    def test_slideshow_has_str(self):
        self.assertIn('__str__', dir(Slideshow), msg='Slideshow has __str__')

class GetTest(TestCase):
    def test_root_redirected_to_slide_list(self):
        c = Client()
        res = c.get('/')
        self.assertEqual(res.status_code, 302, msg='HTTP 302 Moved')
        self.assertEqual(res.url, '/slide/', msg='Redirected to slide list')

    def test_slide_list(self):
        c = Client()
        res = c.get('/slide/')
        self.assertEqual(res.status_code, 200, msg='HTTP 200 OK')
        self.assertTrue(res.has_header('Content-Type'), msg='Has Content-Type')
        self.assertEqual(res.charset, 'utf-8', msg='UTF-8')
        self.assertGreater(len(res.content), 0)

    def test_nonexistent(self):
        c = Client()
        res = c.get('/nonexistent')
        self.assertEqual(res.status_code, 404, msg='HTTP 404 Not Found')

