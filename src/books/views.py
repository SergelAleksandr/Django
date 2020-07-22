from .models import Books
from .forms import CreateBookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView


# class HomePageView(ListView):
#     model = Books
#     template_name = 'books/home.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_books'] = Books.objects.reverse()[:5]
#         return context

class HomePageView(TemplateView):
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = Books.objects.all().order_by('-add_time')[:6]
        context['most_popular'] = Books.objects.all().order_by('-rate')[:6]
        return context

class CreateBook(LoginRequiredMixin, CreateView):
    model = Books
    form_class = CreateBookForm
    template_name = 'books/create_book.html'


class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Books
    form_class = CreateBookForm
    template_name = 'books/update_book.html'
    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs={'pk': self.object.pk})
    

class ListBook(ListView):
    model = Books
    template_name = 'books/list_book.html'
    paginate_by = 10

class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Books
    template_name = 'books/delete_book.html'
    success_url = reverse_lazy('books:list')

class DetailBook(DetailView):
    model = Books
    template_name = 'books/detail_book.html'




