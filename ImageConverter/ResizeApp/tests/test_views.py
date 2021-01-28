from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):

    def test_home_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_add_view(self):
        resp = self.client.get(reverse('add'))
        self.assertEqual(resp.status_code, 200)

    def test_redirect(self):
        resp = self.client.get('/dfgdfgfdgbyyrth')
        self.assertEqual(resp.status_code, 301)
