from .models import Profile, User
from books.models import Books
from genre.models import Genre
from author.models import Author
from django.template import Context
# from cart.models import BooksInCart
from .forms import CreateProfileForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.contenttypes.models import ContentType 
from django.contrib.auth.models import Permission, Group
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic import FormView, UpdateView, DetailView, DeleteView, TemplateView

# class MyGroups(Group):
#     admin, created = Group.objects.get_or_create(name='Admin')
#     customer, created = Group.objects.get_or_create(name='Customers')
#     manager, created = Group.objects.get_or_create(name='Manager')
#     content_type_books = ContentType.objects.get_for_model(Books)
#     content_type_profile = ContentType.objects.get_for_model(Profile)
#     content_type_genre = ContentType.objects.get_for_model(Genre)
#     content_type_author = ContentType.objects.get_for_model(Author)
#     # content_type_cart = ContentType.objects.get_for_model(BooksInCart) 
#     customer.permissions.add(Permission.objects.get(codename='can_view_books', name='Can view books', content_type=content_type_books))
#     customer.permissions.add(Permission.objects.get(codename='can_view_profile', name='Can view profile', content_type=content_type_profile))
#     customer.permissions.add(Permission.objects.get(codename='can_view_genre', name='Can view genre', content_type=content_type_genre))
#     customer.permissions.add(Permission.objects.get(codename='can_view_author', name='Can view author', content_type=content_type_author))
#     # customer.permissions.add(Permission.objects.get(codename='can_add_books_in_cart', name='Can add books in cart', content_type=content_type_cart))
#     # customer.permissions.add(Permission.objects.get(codename='can_change_books_in_cart', name='Can change books in cart', content_type=content_type_cart))
#     # customer.permissions.add(Permission.objects.get(codename='can_delete_books_in_cart', name='Can delete books in cart', content_type=content_type_cart))
#     # customer.permissions.add(Permission.objects.get(codename='can_view_books_in_cart', name='Can view books in cart', content_type=content_type_cart))

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
            raise forms.ValidationError ("Пароли не совпадают")

        user, create=User.objects.get_or_create(
            username=form_username,
            password=form_password,
            first_name=form_first_name,
            last_name=form_last_name,
            email=form_email
        )
        user.groups.add(Group.objects.get(name='Customers'))
        if create:
            user.set_password(form_password)
            user.save()
        profile, create=Profile.objects.get_or_create(
            user=User.objects.get(username=form_username),
            first_name=form_first_name,
            last_name=form_last_name,
            phone_number=form_phone_number,
            address1=form_address1,
            address2=form_address2,
            image=form_image
        )
        if user.is_anonymous:
            user = None

        return HttpResponseRedirect(self.get_success_url())
        
    def get_success_url(self):
        return reverse_lazy('profiles:login_done')

class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profiles/update_profile.html'
    
    def get_success_url(self):
        return reverse_lazy('profile:detail', kwargs={'pk': self.object.pk})

class DeleteProfile(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profiles/delete_profile.html'
    success_url = reverse_lazy('home')

class DetailProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profiles/detail_profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_pk = self.kwargs.get('user_pk')
    #     context['profile'] = Profile.objects.all().filter(pk=user_pk)
    #     return context

# ЛОГИН
class Login(LoginView):
    template_name = 'profiles/login.html'
    
    def get_success_url(self):
       return reverse_lazy('home')

class LoginDone(TemplateView):
    template_name = 'profiles/login_done.html'

class Logout(LogoutView):
    template_name = 'profiles/logout.html'

    def get_success_url(self):
       return reverse_lazy('home')

class PasswordChange(PasswordChangeView):
    template_name = 'profiles/password_change.html'

    def get_success_url(self):
       return reverse_lazy('profiles:password_change_done')

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'profiles/password_change_done.html'

    def get_success_url(self):
       return reverse_lazy('home')

class PasswordReset(PasswordResetView):
    template_name = 'profiles/password_reset.html'

class PasswordResetDone(PasswordResetDoneView):
    template_name = 'profiles/password_reset_done.html'
 
class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'profiles/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'profiles/password_reset_complete.html'







