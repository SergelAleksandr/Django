  
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import admin
from . import models
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from books.models import Books
from cart.models import BookInCart
from cart.models import Cart
from .forms import AddBookToCartForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView

def get_cart(request):
    cart_pk=request.session.get('cart_pk')
    user=request.user
    if user.is_anonymous:
        user=None
    cart, create=models.Cart.objects.get_or_create(
        pk=cart_pk,
        defaults={
            'user':user,
        }
        )
    if create:
        request.session['cart_pk'] = cart.pk
    return cart

class AddBookToCart(SuccessMessageMixin, UpdateView):
    model=models.BookInCart
    form_class=AddBookToCartForm
    template_name='cart/add_to_cart.html'

    def get_success_message(self, *args, **kwargs):
        return f"Книга {self.object.book} добавлена в корзину"

    def get_object(self):
        # cart_pk = self.request.session.get('cart_pk', None)
        book_pk = self.request.GET.get('book_pk')
        book = Books.objects.get(pk=book_pk)
        cart = get_cart(self.request)
        # cart, create = get_cart(self.request)
        # if create:
        #     self.request.session['cart_pk']=cart.pk 
        obj, create = self.model.objects.get_or_create(
            cart = cart,
            book = book,
            defaults={}
        )
        return obj

    def get_success_url(self):
       return reverse_lazy('home')

class CartTotal(RedirectView):

    def get_redirect_url(self):
        cart = get_cart(self.request)
        cart_pk = self.request.session.get('cart_pk')
        return reverse_lazy('cart:detail', kwargs={'pk': self.request.session.get('cart_pk')})


class CartDelete(DeleteView):
    model = BookInCart
    template_name='cart/delete.html'

    def get_success_url(self):
       return reverse_lazy('cart:detail')

class CartDetail(DetailView):
    model = Cart
    template_name='cart/detail_cart.html'

    def get_object(self):
        cart = get_cart(self.request)
        return cart