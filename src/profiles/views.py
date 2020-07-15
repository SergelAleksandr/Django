from .models import Profile, User
from .forms import CreateProfileForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group

from django.views.generic import FormView, UpdateView, ListView, DeleteView, DetailView, TemplateView

class CreateProfile(FormView):
    form_class = CreateProfileForm
    template_name = 'profiles/create_profile.html'

    def form_valid(self, form):
        form_username = form.cleaned_data['username']
        form_password = form.cleaned_data['password']
        form_first_name = form.cleaned_data['first_name']
        form_last_name = form.cleaned_data['last_name']
        form_email = form.cleaned_data['email']
        form_phone_number = form.cleaned_data['phone_number']
        form_address1 = form.cleaned_data['address1']
        form_address2 = form.cleaned_data['address2']
        form_image = form.cleaned_data['image']
        
        if form.cleaned_data['password'] != form.cleaned_data['password1']:
            self.add_error('Проверка пароля', "Пароли не совпадают")

        user, create=User.objects.get_or_create(
            username=form_username,
            password=form_password,
            first_name=form_first_name,
            last_name=form_last_name,
            email=form_email
        )
        user.groups.add(Group.objects.get(name='Customers'))
        profile, create=Profile.objects.get_or_create(
            user=User.objects.get(username=form_username),
            first_name=form_first_name,
            last_name=form_last_name,
            phone_number=form_phone_number,
            address1=form_address1,
            address2=form_address2,
            image=form_image
        )

    def get_success_url(self):
        return reverse_lazy('profile:detail', kwargs={'pk': self.object.pk})


# ЛОГИН
class Login(FormView):
    form_class = LoginForm
    template_name = 'profiles/login.html'
    
    def user_login(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(username=clean_data['username'], password=clean_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return reverse_lazy('profile:detail', kwargs={'pk': self.object.pk})
                else:
                    return reverse_lazy('auth:login')
            else:
                return reverse_lazy('auth:login')




# Изменение
# class UpdateProfile(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = CreateProfileForm
#     template_name = 'profiles/update_profile.html'
#     def get_success_url(self):
#         return reverse_lazy('profile:detail', kwargs={'pk': self.object.pk})
# 
class ListProfile(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/list_profile.html'

class DeleteProfile(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profiles/delete_profile.html'
    success_url = reverse_lazy('profile:list')

class DetailProfile(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/detail_profile.html'





