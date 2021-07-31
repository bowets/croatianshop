from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('delivery_returns/', views.delivery_return, name='delivery_return'),
    path('faq/', views.faq, name='faq'),
]
