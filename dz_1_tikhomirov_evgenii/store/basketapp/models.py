from django.db import models
from django.conf import settings
from mainapp.models import Product

class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super().delete(*args, **kwargs)

class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="baskets")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)

    def _get_product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    product_cost = property(_get_product_cost)

    def _get_total_quantity(self):
        "return total quantity for user"
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    total_quantity = property(_get_total_quantity)


    def total_cost(self):
        "return total cost for user"
        _items = Basket.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost
    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_product(user, product):
        return Basket.objects.filter(user=user, product=product)    \

    @classmethod
    def get_products_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]
        return basket_items_dic

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    def save(self, *args, **kwargs):
        # 1. Как определить сохраняем мы новый объект или изеняем старый
        # 2. Как использовать старые данные при изменении

        # 1.
        if self.pk:
            # Изменяем объект
            print('Значения')
            print('q новое значение', self.quantity)

            # print('q2 старое значение', self.__class__.get_item(self.pk).quantity)
            # old = Basket.objects.get(pk=self.pk).quantity
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            # Это новый объект - создаем
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    # переопределяем метод, удаляющий объект
    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()