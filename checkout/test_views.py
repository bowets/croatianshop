from django.http import response
from django.test import TestCase
from products.models import Product

class TestCheckoutViews(TestCase):
    """Test views in the checkout app are resolving correctly """

    def test_checkout_view_resolves_correctly(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

