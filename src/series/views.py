from .models import Series
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

class CreateSeries(LoginRequiredMixin, CreateView):
    model = Series
    fields = ('name','description')
    template_name = 'series/create_series.html'
    success_url = reverse_lazy('series:list')

class UpdateSeries(LoginRequiredMixin, UpdateView):
    model = Series
    fields = ('name','description')
    template_name = 'series/update_series.html'
    success_url = reverse_lazy('series:list')
    
class ListSeries(ListView):
    model = Series
    template_name = 'series/list_series.html'

class DeleteSeries(LoginRequiredMixin, DeleteView):
    model = Series
    template_name = 'series/delete_series.html'
    success_url = reverse_lazy('series:list')

class DetailSeries(DetailView):
    model = Series
    template_name = 'series/detail_series.html'
