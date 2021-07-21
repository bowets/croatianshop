from django.shortcuts import render

def view_cart(request):
    """Renders the about page"""

    return render(request, 'checkout/checkout.html')
