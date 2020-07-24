from django.urls import path
from order.views import DetailOrder, DeleteOrder, OrderDone, OrderBy, OrderFor
app_name="order"

urlpatterns = [
    path('books_in_order/', OrderBy.as_view(), name='books_in_order'),
    path('detail_order/', DetailOrder.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteOrder.as_view(), name='delete'),
    path('order_done/', OrderDone.as_view(), name='order_done'),
    path('order_for_user/', OrderFor.as_view(), name='order_for_user'),

]