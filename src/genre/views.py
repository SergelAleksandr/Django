from .models import Genre
from .forms import CreateGenreForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView



class CreateGenre(LoginRequiredMixin, CreateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'genres/create_genre.html'


class UpdateGenre(LoginRequiredMixin, UpdateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'genres/update_genre.html'
    def get_success_url(self):
        return reverse_lazy('genres:detail', kwargs={'pk': self.object.pk})
        
class ListGenre(ListView):
    model = Genre
    template_name = 'genres/list_genre.html'

class DeleteGenre(LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = 'genres/delete_genre.html'
    success_url = reverse_lazy('genres:list')

class DetailGenre(DetailView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'genres/detail_genre.html'
