from django.test import TestCase
from django.urls import reverse, resolve
from .views import index, about, delivery_return, faq

# Create your tests here.

class TestURLs(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)


    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_delivery_return_url_is_resolved(self):
        url = reverse('delivery_return')
        self.assertEquals(resolve(url).func, delivery_return)


    def test_faq_url_is_resolved(self):
        url = reverse('faq')
        self.assertEquals(resolve(url).func, faq)