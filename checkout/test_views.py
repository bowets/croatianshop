from django.test import TestCase


class TestCheckoutViews(TestCase):

    def test_checkout_view_resolves_correctly(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
