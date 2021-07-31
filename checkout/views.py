from products.views import product_details
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from products.models import Product


def view_cart(request):
    """Renders the about page"""

    return render(request, 'checkout/checkout.html')


def add_to_cart(request, item_id):
    """Adds items to the cart"""

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated the quantity for \
                        {product.name} to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {cart[item_id]} \
                                 {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update the quantity of items in the cart"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated the quantity for \
                                {product.name} to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name}')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_item_from_cart(request, item_id):
    """Removes an item from the cart"""
    product = get_object_or_404(Product, pk=item_id)

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name}')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
