from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('purchase_success/<order_number>', views.purchase_success, name='purchase_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]