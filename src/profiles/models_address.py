# from django.db import models
# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Address_1(models.Model):
#     address = models.CharField(
#         verbose_name='Адрес:',
#         max_length=20
#     )
#     country = models.CharField(
#         verbose_name='Страна',
#         max_length=20
#     )
#     city = models.CharField(
#         verbose_name='Город',
#         max_length=40
#     )
#     index = models.IntegerField(
#         verbose_name='Индекс',
#         max_length=6,
#         null=True,
#         blank=True
#     )
#     street = models.CharField(
#         verbose_name='Улица',
#         max_length=40
#     )
#     house = models.IntegerField(
#         verbose_name='Дом',
#         max_length=5,
#     )
#     building = models.CharField(
#         verbose_name='Улица',
#         max_length=40,
#         null=True,
#         blank=True
#     )
#     flat = models.IntegerField(
#         verbose_name='Квартира',
#         max_length=3,
#         null=True,
#         blank=True
#     )

#     def __str__(self):
#         return self.address

# class Address_2(models.Model):
#     address = models.CharField(
#         verbose_name='Адрес:',
#         max_length=20
#     )
#     country = models.CharField(
#         verbose_name='Страна',
#         max_length=20
#     )
#     city = models.CharField(
#         verbose_name='Город',
#         max_length=40
#     )
#     index = models.IntegerField(
#         verbose_name='Индекс',
#         max_length=6
#     )
#     street = models.CharField(
#         verbose_name='Улица',
#         max_length=40
#     )
#     house = models.IntegerField(
#         verbose_name='Дом',
#         max_length=5,
#     )
#     building = models.CharField(
#         verbose_name='Улица',
#         max_length=40,
#         null=True,
#         blank=True
#     )
#     flat = models.IntegerField(
#         verbose_name='Квартира',
#         max_length=3,
#         null=True,
#         blank=True
#     )

#     def __str__(self):
#         return self.address