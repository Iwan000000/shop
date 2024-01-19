from django.shortcuts import render

from shoping.models import Category, Product


# Create your views here.
def index(request):
    context = {
        "object_list": Category.objects.all(),
        "title": "мясо свежее"
    }
    return render(request, 'shoping/index.html', context)

def product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        "object_list": Product.objects.filter(category_id=pk),
        "title": f"{category_item.name}"
    }
    return render(request, 'shoping/product.html', context)



def product_information(request, pk):
    # Получить объект товара по его идентификатору
    product = Product.objects.get(pk=pk)

    context = {
        'object': product,  # Передача объекта товара в контекст шаблона
    }

    return render(request, 'shoping/product_information.html', context)
