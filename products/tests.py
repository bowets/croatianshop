from django.shortcuts import resolve_url
from django.test import TestCase
from django.urls import reverse, resolve
from .views import all_products, product_details
from .models import Product


class TestURLs(TestCase):

    def test_shop_url_is_resolved(self):
        url = reverse('shop')
        self.assertEquals(resolve(url).func, all_products)

    def test_product_details_url_is_resolved(self):
        url = reverse('product_details')
        product_id = Product.objects.create(id=100, name="Test Product")
        # url = url.join("/",product_id)
        self.assertEquals(resolve(url).func, product_details)
