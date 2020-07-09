from .models import Author
from .forms import CreateAuthorForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from books.models import Books

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

class CreateAuthor(LoginRequiredMixin, CreateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'author/create_author.html'

class UpdateAuthor(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'author/update_author.html'
    def get_success_url(self):
        return reverse_lazy('author:detail', kwargs={'pk': self.object.pk})
    
class ListAuthor(ListView):
    model = Author
    template_name = 'author/list_author.html'

class DeleteAuthor(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author/delete_author.html'
    success_url = reverse_lazy('author:list')

class DetailAuthor(DetailView):
    model = Author
    template_name = 'author/detail_author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(pk__in=Author.books)
        return context




