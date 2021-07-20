from django.shortcuts import render
from products.models import Product

def index(request):
    """Renders the home page template"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
