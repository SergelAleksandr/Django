from django.db import models
from cart.models import Cart

class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT
    )
    status = models.CharField(
        choices=[
        ('1','Новый'),
        ('2','Подтвержден'),
        ('3','В обработке'),
        ('4','Доставляется'),
        ('5','Доставлен'),
        ('6','Отменен'),],
        max_length=1,
        blank=False,
        default='Новый',
    )
    delivery_address = models.CharField(
        verbose_name="Адрес доставки", 
        max_length=150
    )
    contact_phone = models.CharField(
        verbose_name="Номер телефона", 
        max_length=20
    )
    created = models.DateTimeField(
        verbose_name="Создано", 
        auto_now=False, 
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Изменено", 
        auto_now=True, 
        auto_now_add=False
    )