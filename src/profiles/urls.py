from django.urls import path
from profiles.views import  ListProfile, DeleteProfile, DetailProfile, Login
from . import views
app_name = 'profile'

urlpatterns = [
    # path('update_profile/<int:pk>', views.UpdateProfile.as_view(), name='update'),
    path('list_profile/', views.ListProfile.as_view(), name='list'),
    path('delete_profile/<int:pk>', views.DeleteProfile.as_view(), name='delete'),
    path('detail_profile/<int:pk>', views.DetailProfile.as_view(), name='detail'),
    path('create_profile/', views.CreateProfile.as_view(), name='create'),
    path('login/', views.Login.as_view(), name='login'),

] 