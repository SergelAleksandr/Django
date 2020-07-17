from django.contrib import admin
from cart.models import Cart, BookInCart

admin.site.register(Cart)
admin.site.register(BookInCart)