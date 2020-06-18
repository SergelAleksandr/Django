from django.urls import path
from books.views import CreateBook, UpdateBook, ListBook, DeleteBook, DetailBook, HomePageView
from . import views
app_name = 'books'

urlpatterns = [
    path('create_book/', views.CreateBook.as_view(), name='create'),
    path('update_book/<int:pk>', views.UpdateBook.as_view(), name='update'),
    path('list_book/', views.ListBook.as_view(), name='list'),
    path('delete_book/<int:pk>', views.DeleteBook.as_view(), name='delete'),
    path('detail_book/<int:pk>', views.DetailBook.as_view(), name='detail'),
    path('home/', views.HomePageView.as_view(), name='home')
] 
