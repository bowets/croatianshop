from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product


class TestPurchaseOrderModel(TestCase):

    def test_billing_address(self):
        billing_address = Order(full_name='Test Billing Name',
                                street_address1='Test Address1',
                                street_address2='Test Address2',
                                town_or_city='Test City',
                                eircode='Test Postcode',
                                country='Test Country')

        self.assertEqual(billing_address.full_name, 'Test Billing Name')
        self.assertEqual(billing_address.street_address1, 'Test Address1')
        self.assertEqual(billing_address.street_address2, 'Test Address2')
        self.assertEqual(billing_address.town_or_city, 'Test City')
        self.assertEqual(billing_address.eircode, 'Test Postcode')
        self.assertEqual(billing_address.country, 'Test Country')

    def test_request_order(self):
        order = Order(order_total=999.00, email='testmode@gmail.com')
        order.save()
        self.assertEqual(order.order_total, 999.00)
        self.assertEqual(order.email, 'testmode@gmail.com')


class TestCheckoutOrderLineItem(TestCase):

    def test_check_order_exists(self):
        order_number = Order(id=1, order_total=66.00)
        order_number.save()
        product = Product(price=66.00, featured=False)
        product.save()
        orderLineItem = OrderLineItem(product=product,
                                      quantity=1,
                                      order=order_number,
                                      lineitem_total=66.00)

        orderLineItem.save()
        self.assertEqual(orderLineItem.product, product)
        self.assertEqual(orderLineItem.quantity, 1)
        self.assertEqual(orderLineItem.lineitem_total, 66.00)
