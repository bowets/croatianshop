from django.shortcuts import render

def index(request):
    """Renders the home page template"""
    return render(request, 'home/index.html')
