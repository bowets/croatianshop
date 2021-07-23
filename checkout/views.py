from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from products.models import Product

def view_cart(request):
    """Renders the about page"""

    return render(request, 'checkout/checkout.html')


def add_to_cart(request, item_id):
    """Adds items to the cart"""

    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')


    request.session['cart'] = cart
    return redirect(redirect_url)



def update_cart(request, item_id):
    """Update the quantity of items in the cart"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)


    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_item_from_cart(request, item_id):
    """Removes an item from the cart"""
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)