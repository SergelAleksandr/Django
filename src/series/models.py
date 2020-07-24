from django.db import models


class Series(models.Model):
    name = models.CharField(
        verbose_name="Название серии",
        max_length=50,
        null=True,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание серии",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("series:list")