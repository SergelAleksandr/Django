from .models import Publisher
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from django.views.generic import CreateView, UpdateView, ListView, DeleteView

class CreatePublisher(LoginRequiredMixin, CreateView):
    model = Publisher
    fields = ('name',)
    template_name = 'publisher/create_publisher.html'
    success_url = reverse_lazy('publisher:list')

class UpdatePublisher(LoginRequiredMixin, UpdateView):
    model = Publisher
    fields = ('name',)
    template_name = 'publisher/update_publisher.html'
    success_url = reverse_lazy('publisher:list')
    
class ListPublisher(ListView):
    model = Publisher
    template_name = 'publisher/list_publisher.html'

class DeletePublisher(LoginRequiredMixin, DeleteView):
    model = Publisher
    template_name = 'publisher/delete_publisher.html'
    success_url = reverse_lazy('publisher:list')


