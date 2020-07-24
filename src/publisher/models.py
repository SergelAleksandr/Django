from django.db import models


class Publisher(models.Model):
    name=models.CharField(
        verbose_name="Название",
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("publisher:list")