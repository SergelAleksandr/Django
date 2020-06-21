from django.db import models
from django.urls import reverse_lazy



# Create your models here.
class Genre(models.Model):
    # pk PK + autoincrement not null
    name = models.CharField(
        verbose_name='Название жанра',
        max_length=120
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
    