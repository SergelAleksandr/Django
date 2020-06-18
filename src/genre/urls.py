from django.urls import path
from genre.views import CreateGenre, UpdateGenre, ListGenre, DeleteGenre, DetailGenre
from . import views
app_name = 'genres'

urlpatterns = [
    path('create_genre/', views.CreateGenre.as_view(), name='create'),
    path('update_genre/<int:pk>', views.UpdateGenre.as_view(), name='update'),
    path('list_genre/', views.ListGenre.as_view(), name='list'),
    path('delete_genre/<int:pk>', views.DeleteGenre.as_view(), name='delete'),
    path('detail_genre/<int:pk>', views.DetailGenre.as_view(), name='detail'),
]
