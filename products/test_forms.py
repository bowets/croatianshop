from products.forms import ProductForm
from django.test import TestCase
from .forms import ProductForm

class TestProductForm(TestCase):
    """Test that the product forms required fields work"""

    def test_create_product_form_incomplete_is_not_valid(self):
        form = ProductForm({
            'name': 'test name',
            'description': 'test description',
            'price': None,
            'featured': True, 
        })

        self.assertFalse(form.is_valid())


    def test_create_product_form_complete_is_valid(self):
        form = ProductForm({
            'name': 'test name',
            'description': 'test description',
            'price': 66.00,
            'featured': True, 
        })

        self.assertTrue(form.is_valid())
