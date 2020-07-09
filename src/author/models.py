from django.db import models
from django.urls import reverse_lazy

class Author(models.Model):
    name = models.CharField(
        verbose_name='Имя автора',
        max_length=100
    )
    birth = models.IntegerField(
        verbose_name='Год рождения',
        null=True,
        blank=True
    )
    biography = models.TextField(
        verbose_name='Биография',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фотография автора',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("author:list")

