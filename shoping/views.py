from django.shortcuts import render

from shoping.models import Category, Product


# Create your views here.
def index(request):
    context = {
        "object_list": Product.objects.all(),
        "title": "мясо свежее"
    }
    return render(request, 'shoping/index.html', context)


#
