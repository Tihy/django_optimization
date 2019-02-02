from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
from authapp.models import ShopUserProfile

import json, os

JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            # category = ProductCategory.objects.get(name=category_name)
            # new_product = Product(name=product['name_product'], short_desc=product['short_desc'], category=category)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
    super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
