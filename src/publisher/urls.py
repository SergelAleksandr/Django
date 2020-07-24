from django.urls import path
from publisher.views import CreatePublisher, UpdatePublisher, ListPublisher, DeletePublisher
from . import views
app_name = 'publisher'

urlpatterns = [
    path('create_publisher/', views.CreatePublisher.as_view(), name='create'),
    path('update_publisher/<int:pk>', views.UpdatePublisher.as_view(), name='update'),
    path('list_publisher/', views.ListPublisher.as_view(), name='list'),
    path('delete_publisher/<int:pk>', views.DeletePublisher.as_view(), name='delete'),
] 
