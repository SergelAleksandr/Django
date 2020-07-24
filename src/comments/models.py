from django.db import models
from books.models import Books
from order.models  import Order

class CommentsBook(models.Model):
    book = models.ForeignKey(
        Books, 
        verbose_name='Книга',
        on_delete=models.PROTECT,
        related_name='comments'
        )
    user = models.CharField(
        verbose_name='Имя',
        max_length=50
        )
    body = models.TextField(
        verbose_name='Комментарий'
    )
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
        auto_now_add=False
    )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

# class CommentsOrder(models.Model):
#     order = models.ForeignKey(Order, related_name='comments', on_delete=models.PROTECT)
#     user = models.CharField(max_length=80)
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ('created',)

#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.name, self.order)