from django.shortcuts import get_object_or_404, render
from .models import Product

def all_products(request):
    """A view to return all products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop.html', context)


def product_details(request, product_id):
    """A view to a page to display a specific products details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)