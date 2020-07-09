from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
# from .models_address import Address_1, Address_2
from django.urls import reverse_lazy

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # @receiver(post_save, sender=User)
    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         profile = Profile.objects.create(user=instance)
    #     instance.profile.save()

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=15
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=15
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=50
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=50
    )
    email = models.EmailField(
        verbose_name='E-mail'
    )
    phone_number = models.IntegerField(
        verbose_name='Номер телефона',
    )
    # address_1 = models.ForeignKey(
    #     Address_1,
    #     on_delete=models.CASCADE
    # )
    # address_2 = models.ForeignKey(
    #     Address_2,
    #     on_delete=models.CASCADE
    # )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='profile_image',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("books:home")

# class Address(models.Model):
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
#         max_length=3
#     )
#     flat = models.IntegerField(
#         verbose_name='Квартира',
#         max_length=3
#     )

#     def __str__(self):
#         return self.address