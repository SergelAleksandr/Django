from .models import Profile
from .forms import CreateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import login

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView



    # def my_view(request):
    # username = request.POST['email']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)

    # else:
    #     # Return an 'invalid login' error message.
    #     ...

class CreateProfile(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profiles/create_profile.html'
    def get_success_url(self):
        return reverse_lazy('profile:detail', kwargs={'pk': self.object.pk})

class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profiles/update_profile.html'
    def get_success_url(self):
        return reverse_lazy('profile:detail', kwargs={'pk': self.object.pk})

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





