from django.db import models
from django.urls import reverse_lazy
from genre.models import Genre
from author.models import Author
from series.models import Series
from publisher.models import Publisher

class Books(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=100
    )
    author = models.ManyToManyField(
        Author,
        verbose_name='Автор',
        related_name='books'
    )
    series = models.ForeignKey(
        Series,
        verbose_name='Серия книг',
        related_name='series',
        on_delete=models.PROTECT
    )
    description = models.TextField(
        verbose_name='Описание книги',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='books'
    )
    image = models.ImageField(
        verbose_name='Обложка книги',
        upload_to='book_cover',
        null=True,
        blank=False
    )
    price = models.FloatField(
        verbose_name='Стоимость книги',
    )
    year = models.IntegerField(
        verbose_name='Год издания',
    )
    quantity = models.IntegerField(
        verbose_name='Количество страниц',
    )
    binding = models.CharField(
        verbose_name='Переплет',
        max_length=100
    )
    forma = models.CharField(
        verbose_name='Формат',
        max_length=10
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=20
    )
    weight = models.IntegerField(
        verbose_name='Вес (гр.)',
    )
    age = models.IntegerField(
        verbose_name='Возрастные ограничения',
    )
    publisher = models.ForeignKey(
        Publisher,
        verbose_name='Издательство',
        related_name='publisher',
        on_delete=models.PROTECT
    )
    rate = models.IntegerField(
        verbose_name='Рейтинг (0-10)',
    )
    add_time = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now=False,
        auto_now_add=True
    )
    update_time = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("books:list")
