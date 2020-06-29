from django.urls import path
from profiles.auth_views import Login
from . import auth_views
app_name = 'auth'

urlpatterns = [
    path('login/', auth_views.Login.as_view(), name='login'),
] 