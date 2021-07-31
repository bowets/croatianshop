from django.shortcuts import render
from products.models import Product


def index(request):
    """Renders the home page template"""

    featured_products = Product.objects.filter(featured=True)
    count = featured_products.count()
    context = {
        'featured_products': featured_products,
        'count': count,
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
