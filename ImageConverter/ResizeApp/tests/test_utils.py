from PIL import Image
from django.test import TestCase

from ResizeApp.utils import reformat_image, gen_name


class ReformatImageTestCase(TestCase):

    def test_resize_width_and_height(self):
        name = 'test\\test' + gen_name() + 'png'
        img = Image.new('RGB', (60, 30), color='red')
        img.save(name)
        reformat_image(name, name, 100, 50)
        img = Image.open(name)
        self.assertEqual((100, 50), img.size)

    def test_resize_width_only(self):
        name = 'test\\test' + gen_name() + 'png'
        img = Image.new('RGB', (60, 30), color='red')
        img.save(name)
        reformat_image(name, name, 100, '')
        img = Image.open(name)
        self.assertEqual((100, 50), img.size)

    def test_resize_height_only(self):
        name = 'test\\test' + gen_name() + 'png'
        img = Image.new('RGB', (60, 30), color='red')
        img.save(name)
        reformat_image(name, name, '', 50)
        img = Image.open(name)
        self.assertEqual((100, 50), img.size)

    def test_resize_bad_values(self):
        name = 'test\\test' + gen_name() + 'png'
        img = Image.new('RGB', (60, 30), color='red')
        img.save(name)
        reformat_image(name, name, 50, 50)
        img = Image.open(name)
        self.assertEqual((60, 30), img.size)
