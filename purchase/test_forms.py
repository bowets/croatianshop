from django.test import TestCase
from .forms import OrderForm

class TestCheckoutForms(TestCase):

    def test_order_form_is_valid_with_required_fields_filled(self):
        order_form = OrderForm({
            'order_number': 'adsfafasdf',
            'full_name': 'test name',
            'email': 'email@email.com',
            'phone_number': '3344234',
            'country': 'IE',
            'eircode': 'd11',
            'town_or_city': 'dublin',
            'street_address1': 'street1',
            'street_address2': 'street2',
            'county': 'Dublin',
            'delivery_cost': '0',
            'order_total': '444',
            'grand_total': '444',
            'original_cart': '23423424',
            'stripe_pid': '23423432434234',
            })
        self.assertTrue(order_form.is_valid())

    def test_order_form_is_not_valid_if_full_name_is_empty(self):
        order_form = OrderForm({
            'full_name':None,
            'phone_number':'123456',  
            'street_address1':'street1',
            'street_address2':'street2',
            'town_or_city':'Dublin',
            'county':'Dublin',
            'eircode':'D11',
            'country':'Ireland'
            })
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['full_name'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_phone_number_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':None, 
            'street_address1':'street1',
            'street_address2':'street2',
            'town_or_city':'Dublin',
            'county':'Dublin',
            'eircode':'D11',
            'country':'Ireland'
            })
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['phone_number'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_street_address1_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'123456',  
            'street_address1':None,
            'street_address2':'street2',
            'town_or_city':'Dublin',
            'county':'Dublin',
            'eircode':'D11',
            'country':'Ireland'
            })
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['street_address1'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_town_or_city_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'123456',  
            'street_address1':'street1',
            'street_address2':'street2',
            'town_or_city':None,
            'county':'Dublin',
            'eircode':'D11',
            'country':'Ireland' })
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['town_or_city'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_country_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'123456',  
            'street_address1':'street1',
            'street_address2':'street2',
            'town_or_city':'Dublin',
            'county':'Dublin',
            'eircode':'D11',
            'country':None 
            })
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['country'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_postcode_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'123456',  
            'street_address1':'street1',
            'street_address2':'street2',
            'town_or_city':'Dublin',
            'county':'Dublin',
            'eircode':None,
            'country':'Ireland'})
        self.assertFalse(order_form.is_valid())
