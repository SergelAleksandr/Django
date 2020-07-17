from django.urls import path
from cart.views import AddBookToCart, CartDelete, CartDetail, CartTotal
from . import views
app_name = 'cart'

urlpatterns = [
    path('add_to_cart/', views.AddBookToCart.as_view(), name='add'),
    path('cart_total', views.CartTotal.as_view(), name='total'),
    path('delete_cart/<int:pk>', views.CartDelete.as_view(), name='delete'),
    path('detail_cart', views.CartDetail.as_view(), name='detail'),
] 
