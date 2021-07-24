from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import OrderForm



def purchase(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart at the moment")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'purchase/purchase.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J8TH6JCvONQIszN8CmraPKb2feb0d8dbpiyyQVp04gdk4JAfOOobiXanmWd8o09EJV12hocqJbYhyJuzC43d3LC00VARaiq8D',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

        
