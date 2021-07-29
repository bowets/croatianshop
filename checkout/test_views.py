from django.http import response
from django.test import TestCase
from products.models import Product

class TestCheckoutViews(TestCase):
    """Test views in the checkout app are resolving correctly """

    def test_checkout_view_resolves_correctly(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_add_to_cart_view(self):
        product = Product(name='test_product')
        response = self.client.get(f'/add/{product.id}')
        self.assertEqual(response.status_code, 200)