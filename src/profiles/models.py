from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True
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
        verbose_name='email'
    )
    image = models.ImageField(
        verbose_name='Авка',
        upload_to='profile_image',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("books:home")

    # class Meta:
    #     permissions = [
    #         ('can_eat_pizzas', 'Can eat pizzas')
    #         ]