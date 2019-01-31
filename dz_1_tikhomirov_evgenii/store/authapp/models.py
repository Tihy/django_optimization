from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

class ShopUser (AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    active_key = models.CharField(max_length=120, verbose_name='код подтверждения', blank=True)
    active_key_expires = models.DateTimeField(
        verbose_name='актуальность ключа',
        default=(now() + timedelta(hours=48)))
# Create your models here.
    def is_active_key_expired(self):
        if now() <= self.active_key_expires:
            return False
        else:
            return True