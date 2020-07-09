from django.urls import path
from author.views import CreateAuthor, UpdateAuthor, ListAuthor, DeleteAuthor, DetailAuthor
from . import views
app_name = 'author'

urlpatterns = [
    path('create_author/', views.CreateAuthor.as_view(), name='create'),
    path('update_author/<int:pk>', views.UpdateAuthor.as_view(), name='update'),
    path('list_author/', views.ListAuthor.as_view(), name='list'),
    path('delete_author/<int:pk>', views.DeleteAuthor.as_view(), name='delete'),
    path('detail_author/<int:pk>', views.DetailAuthor.as_view(), name='detail'),
] 
