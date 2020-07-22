from django.urls import path
from profiles.views import CreateProfile, UpdateProfile, DeleteProfile, DetailProfile, Login, LoginDone, Logout, PasswordChange, PasswordChangeDone, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete
from . import views
app_name = 'profile'

urlpatterns = [
    path('update_profile/<int:pk>', views.UpdateProfile.as_view(), name='update'),
    path('delete_profile/<int:pk>', views.DeleteProfile.as_view(), name='delete'),
    path('detail_profile/<int:pk>', views.DetailProfile.as_view(), name='detail'),
    path('create_profile/', views.CreateProfile.as_view(), name='create'),
    path('login/', views.Login.as_view(), name='login'),
    path('login_done/', views.LoginDone.as_view(), name='login_done'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    
] 