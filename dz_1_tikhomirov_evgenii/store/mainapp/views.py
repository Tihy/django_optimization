from django.shortcuts import render, get_object_or_404
import datetime
import json, random
from django.conf import settings
import os
from .models import Product, ProductCategory
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


JSON_PATH = 'mainapp/json'

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)




def getHotProduct():
        products = Product.objects.filter(is_active=True, category__is_active=True)
        return random.sample(list(products), 1)[0]


# def getSameProducts(product):
#         same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]
#
#         return same_products








def main(request):
    request.session['param'
    ]= 'Данные сесии'
    books_name = [{'name': 'Fantasy'}, {'name': 'Poem'}, {'name': 'Roman'}, {'name': 'Detective'}]
    example_list=[
        {'name': 'For men', 'text': 'If you do not know what to give, try this', 'image': '/static/img/exclusive/exclusive-1.jpg'},
        {'name': 'For kids', 'text': 'If you do not know what to give, try this', 'image': '/static/img/exclusive/exclusive-2.jpg'},
        {'name': 'For women', 'text': 'If you do not know what to give, try this', 'image': '/static/img/exclusive/exclusive-3.jpg'},
        {'name': 'For work', 'text': 'If you do not know what to give, try this', 'image': '/static/img/exclusive/exclusive-4.jpg'},
    ]
    trend_book = [
        {'name': 'Amazing book', 'text': 'Read and open new breathtaking word of opportunites!', 'image': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
        {'name': 'Amazing book', 'text': 'Read and open new breathtaking word of opportunites!', 'image': '/static/img/trends/internet-business-2703460_960_720.png'},
        {'name': 'Amazing book', 'text': 'Read and open new breathtaking word of opportunites!', 'image': '/static/img/trends/book-cover-2703449_960_720.png'},
        {'name': 'Amazing book', 'text': 'Read and open new breathtaking word of opportunites!',
         'image': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
        {'name': 'Amazing book', 'text': 'Read and open new breathtaking word of opportunites!',
         'image': '/static/img/trends/internet-business-2703460_960_720.png'},
        {'name': 'Amazing book', 'text': 'Read and open new breathtaking word of opportunites!',
         'image': '/static/img/trends/book-cover-2703449_960_720.png'},


    ]

    visit_date = datetime.datetime.now()
    return render(request, 'index.html', {'title': 'Main', 'visit_date': visit_date, 'books': books_name, 'examples': example_list, 'trend': trend_book})


def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)

    if pk:
        if pk == '0':
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            # все объекты
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        # экземпляр класса Paginator 2- сколько объектов на странице
        paginator = Paginator(products, 2)
        try:
            # получение объектов нужной сраницы
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            # последняя страница
            products_paginator = paginator.page(paginator.num_pages)

        print(type(products))
        print(type(products_paginator))

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }

        return render(request, 'products_list.html', content)

    hot_product = getHotProduct()

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,

    }

    return render(request, 'products.html', content)


def contacts(request):
    param = request.session.get('param', 'no')

    names=[
        {'name': 'Moscow', 'Email': 'infomoscow@bookread.com'},
        {'name': 'Berlin', 'Email': 'infoberlin@bookread.com'},
        {'name': 'Paris', 'Email': 'infoparis@bookread.com'},
    ]
    return render(request, 'contacts.html', {'title': 'Contacts', 'contacts': names,'param':param})


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    content = {
        'title': title,
        'links_menu': links_menu,
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'product.html', content)
