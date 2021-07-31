from django.test import TestCase


class TestHomeViews(TestCase):

    def test_about_view_resolves_correctly(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_delivery_return_view_resolves_correctly(self):
        response = self.client.get('/delivery_returns/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/delivery_return.html')

    def test_faq_view_resolves_correctly(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/faq.html')

    def test_index_view_resolves_correctly(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
