from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=20),
    password = forms.CharField(widget=forms.PasswordInput)

class CreateProfileForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=15),
    password = forms.CharField(label='Пароль', max_length=15),
    password1 = forms.CharField(label='Повторите пароль', max_length=15),
    first_name = forms.CharField(label='Имя', max_length=50),
    last_name = forms.CharField(label='Фамилия', max_length=50),
    email = forms.EmailField(label='Email'),
    phone_number = forms.IntegerField(label='Номер телефона'),
    address1 = forms.CharField(label='Адрес доставки основной', max_length=500),
    address2 = forms.CharField(label='Адрес доставки дополнительный', max_length=500),
    image = forms.ImageField(label='Изображение')
