from django.urls import path
from series.views import CreateSeries, UpdateSeries, ListSeries, DeleteSeries, DetailSeries
from . import views
app_name = 'series'

urlpatterns = [
    path('create_series/', views.CreateSeries.as_view(), name='create'),
    path('update_series/<int:pk>', views.UpdateSeries.as_view(), name='update'),
    path('list_series/', views.ListSeries.as_view(), name='list'),
    path('delete_series/<int:pk>', views.DeleteSeries.as_view(), name='delete'),
    path('detail/<int:pk>', views.DetailSeries.as_view(), name='detail'),
] 
