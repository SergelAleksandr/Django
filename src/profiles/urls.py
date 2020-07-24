from django.urls import path
from profiles.views import CreateProfile, UpdateProfile, DeleteProfile, DetailProfile, Login, LoginDone, Logout, PasswordChange, PasswordChangeDone
from . import views
app_name = 'profile'

urlpatterns = [
    path('update_profile/<int:pk>', UpdateProfile.as_view(), name='update'),
    path('delete_profile/<int:pk>', DeleteProfile.as_view(), name='delete'),
    path('detail_profile/<int:pk>', DetailProfile.as_view(), name='detail'),
    path('create_profile/', CreateProfile.as_view(), name='create'),
    path('login/', Login.as_view(), name='login'),
    path('login_done/', LoginDone.as_view(), name='login_done'),
    path('logout/', Logout.as_view(), name='logout'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDone.as_view(), name='password_change_done'),
] 