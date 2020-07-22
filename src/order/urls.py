from django.urls import path
from order.views import Order
from order.views import DetailOrder, DeleteOrder
app_name="order"

urlpatterns = [

    path('books_in_order/', Order.as_view(), name='books_in_order'),
    path('detail_order/', DetailOrder.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteOrder.as_view(), name='delete'),


]