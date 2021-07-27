from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='shop'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('add/', views.add_product, name='add_products'),
]