from PIL import Image
from django.test import TestCase

from ResizeApp.forms import ImageForm


class TestForm(TestCase):

    def test_link(self):
        data = {
            'link': 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            'image': None
        }
        form = ImageForm(data=data)
        self.assertTrue(form.is_valid())

    def test_null(self):
        data = {
            'link': None,
            'image': None
        }
        form = ImageForm(data=data)
        self.assertTrue(form.is_valid())