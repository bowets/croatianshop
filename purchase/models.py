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
    eircode = models.CharField(max_length=10, null=True, blank=true)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
