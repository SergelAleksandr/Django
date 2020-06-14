from django.db import models
from django.urls import reverse_lazy



# Create your models here.
class Genre(models.Model):
    # pk PK + autoincrement not null
    name = models.CharField(
        verbose_name='Название жанра',
        max_length=100,
    )
    description = models.TextField(
        verbose_name='Описание жанра',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy ("genres:list")
    
    

class Book(models.Model):
    # pk PK + autoincrement not null
    name = models.CharField(
        verbose_name='Название книги',
        max_length=100
    )
    # genre = models.ForeignKey(
    #     Genre,
    #     on_delete=models.PROTECT,
    #     verbose_name='Жанр книги',
    # )
    description = models.TextField(
        verbose_name='Описание книги',
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.name
