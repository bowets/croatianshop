from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Product, Category

def all_products(request):
    """A view to return all products"""

    products = Product.objects.all().order_by('name')
    products_count = products.count()
    query = None
    category = None
    categories = Category.objects.all().order_by('name')
    current_category = None
    sort = None
    direction = None
    product_sort = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__id=category)
            current_category = Category.objects.get(id=category)
            products_count = products.count()

            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search term.")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(manufacturer__name__icontains=query)
            products = products.filter(queries)
            products_count = products.count()


        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortkey = sort
            if sortkey == "name":
                sortkey == "lower_name"
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == "manufacturer":
                sortkey = "manufacturer__name"
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        product_sort = f"{sort}_{direction}"

        print(product_sort)
        

    context = {
        'products': products,
        'search_term': query,
        'current_category': current_category,
        'categories': categories,
        'products_count': products_count,
        'product_sort': product_sort,
    }

    return render(request, 'products/shop.html', context)


def product_details(request, product_id):
    """A view to a page to display a specific products details"""
    cart_product_quantity = None
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    if product_id in list(cart.keys()):
        cart_product_quantity = cart[product_id]
    
    context = {
        'product': product,
        'cart_product_quantity': cart_product_quantity,
    }

    return render(request, 'products/product_details.html', context)