from os import truncate
from unittest.result import failfast
from products.models import Product
from django.db import models
import uuid

from django.db.models.fields import EmailField
from django.db.models import Sum
from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, null=False, blank=False)
    eircode = models.CharField(max_length=10, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


    def _generate_order_number(self):
        """Generate random order number"""
        return uuid.uuid4().hex.upper()


    def update_totals(self):
        """Update grand total whenever a line item is added"""

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        
        self.grand_total = self.order_total + self.delivery_cost
        self.save()


    
    def save(self, *args, **kwargs):
        """If there is no order number in an order, this function will generate and save"""
        if not self.order_number:
            self.order_number = self._generate_order_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """If there is no order number in an order, this function will generate and save"""
        
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'


