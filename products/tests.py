from django.shortcuts import resolve_url
from django.test import TestCase
from django.urls import reverse, resolve
from .views import all_products, product_details
from .models import Product


class TestURLs(TestCase):

    def test_shop_url_is_resolved(self):
        url = reverse('shop')
        self.assertEquals(resolve(url).func, all_products)


