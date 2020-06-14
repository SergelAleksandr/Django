from .models import Genre, Book
from .forms import CreateGenreForm
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

class Test(TemplateView):
    template_name = 'testapp/test.html'
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateGenre(CreateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/create_genre.html'


class UpdateGenre(UpdateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/update_genre.html'
    def get_success_url(self):
        return reverse_lazy('genres:detail', kwargs={'pk': self.object.pk})

class ListGenre(ListView):
    model = Genre
    template_name = 'testapp/list_genre.html'

class DeleteGenre(DeleteView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/delete_genre.html'
    success_url = reverse_lazy('genres:list')

class DetailGenre(DetailView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/detail_genre.html'
