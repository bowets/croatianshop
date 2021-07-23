from products.models import Product
from django.test import TestCase
from django.urls import reverse, resolve
from .views import index

# Create your tests here.

class TestURLs(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(url)
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
