from .models import Genre, Book
from .forms import CreateGenreForm

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

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
    success_url = '/list_genre/'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class UpdateGenre(UpdateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/update_genre.html'
    success_url = '/list_genre/'

class ListGenre(ListView):
    model = Genre
    template_name = 'testapp/list_genre.html'

class DeleteGenre(DeleteView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/delete_genre.html'
    success_url = '/list_genre/'