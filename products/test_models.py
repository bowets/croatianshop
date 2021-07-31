from django.test import TestCase
from .models import Product, Category


class TestProductModel(TestCase):

    def test_string_representation(self):
        product = Product.objects.create(name="Test products",
                                         description="Test description",
                                         price=255.99)
        self.assertEqual(str(product), product.name)

    def test_category_name_created_successfully(self):
        category = Category.objects.create(
            name='frozen',
            friendly_name='Frozen',
        )
        self.assertTrue(category.friendly_name)
        self.assertTrue(category.name)

    def test_category_failed_to_create_with_no_name(self):
        category = Category.objects.create(
            friendly_name='Test Category',
        )
        self.assertEqual(str(category), category.name)
