from .models import Category


def category_list(request):
    categories = Category.objects.all().order_by('name')

    context = {
        'categories': categories,
    }

    return context


