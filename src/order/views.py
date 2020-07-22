from django.shortcuts import render, get_object_or_404
from . import models
from .forms import OrderForm
from profiles.models import Profile, User
from django.views.generic import UpdateView, DetailView, DeleteView
from .models import Order
from cart.models import Cart, BookInCart
from django.urls import reverse_lazy
from cart.views import get_cart
from django.contrib.messages.views import SuccessMessageMixin

class Order(UpdateView):
    model = Order
    template_name = 'order/books_in_order.html'
    form_class = OrderForm
    
    def get_object(self):
        user = self.request.user
        if user.is_authenticated and not user.is_superuser:
            user_pk = user.pk
            profile = Profile.objects.get(user=user_pk)
            phone = profile.phone_number
            address = profile.address1
            # address2 = profile.address2
        else:
            phone=''
            address=''

        cart_id = self.request.session.get('cart_pk')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            try:
                order_pk = cart.order.pk
            except:
                order_pk = None

        obj, create = self.model.objects.get_or_create(
            pk = order_pk,
            defaults = {
            'cart':cart,
            'contact_phone':phone,
            'delivery_address':address,
            'status':'Новый',
            }
       )
        return obj

    def get_success_url(self):
        self.object.status = ('2','Подтвержден')
        self.object.save()
        del(self.request.session['cart_pk'])
        return reverse_lazy('home')

class DetailOrder(DetailView):
    model = Order
    template_name = 'order/detail_order.html'
    context_object_name = 'object'
    success_url = reverse_lazy('home')
   
class DeleteOrder(DeleteView):
    model = Order
    template_name='order/delete_order.html'
    success_url = reverse_lazy('books:list')