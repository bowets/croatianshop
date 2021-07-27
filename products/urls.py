from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='shop'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_products, name='add_products'),
]