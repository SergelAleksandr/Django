  
from django.shortcuts import render, redirect
from django.contrib import admin
from . import models
from django.views.generic import UpdateView, DeleteView, DetailView
from books.models import Books
from cart.models import BookInCart, Cart
from .forms import AddBookToCartForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

def get_cart(request):
    cart_pk = request.session.get('cart_pk')
    user = request.user
    if user.is_anonymous:
        user = None
    if cart_pk is not None:
        cart_pk = int(cart_pk)
    cart, create = models.Cart.objects.get_or_create(
        pk=cart_pk,
        defaults={
            'user':user,
        }
        )
    return cart, create

class AddBookToCart(UpdateView):
    model = models.BookInCart
    fields = ['quantity']
    template_name = 'cart/add_to_cart.html'
    success_url = reverse_lazy('cart:detail')

    def get_object(self):
        book_pk = self.request.GET.get('book_pk')
        book = Books.objects.get(pk=int(book_pk))
        cart, create = get_cart(self.request)
        if create:
            self.request.session['cart_pk'] = cart.pk
        obj, create = self.model.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={}
        )
        return obj

class CartDelete(DeleteView):
    model = BookInCart
    template_name='cart/delete_cart.html'

    def get_success_url(self):
       return reverse_lazy('cart:detail')

class CartDetail(DetailView):
    model = Cart
    template_name='cart/detail_cart.html'

    def get_object(self):
        cart = get_cart(self.request)
        cart, create = get_cart(self.request)
        if create:
            self.request.session['cart_pk'] = cart.pk
        return cart