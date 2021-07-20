from django.shortcuts import render
from products.models import Product

def index(request):
    """Renders the home page template"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """Renders the about page"""
    return render(request, 'home/about.html')


def delivery_return(request):
    """Renders the delivery and returns page"""
    return render(request, 'home/delivery_return.html')


def faq(request):
    """Renders the FAQ page"""
    return render(request, 'home/faq.html')