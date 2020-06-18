from django.db import models
from django.urls import reverse_lazy
from genre.models import Genre

class Books(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=100
    )
    author = models.CharField(
        verbose_name='Автор книги',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание книги',
        null=True,
        blank=True
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT
    )
    image = models.ImageField(
        verbose_name='Обложка книги',
        upload_to='book_cover',
        null=True,
        blank=True
    )
    price = models.IntegerField(
        verbose_name='Стоимость книги',
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy ("books:list")