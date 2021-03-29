from django.forms import Textarea, DateTimeField
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from .models import ProxyList


class HomePageView(ListView):
    model = ProxyList
    template_name = 'index.html'
    context_object_name = 'all_proxy_list'


class AddPageView(CreateView):
    model = ProxyList
    template_name = 'add.html'
    fields = ['project', 'proxy_port_out', 'proxy_name', 'fp_name',
              'author', 'stop_date', 'start_date']


class EditView(ListView):
    model = ProxyList
    template_name = 'edit.html'
    context_object_name = 'all_proxy_list'


class DelPageView(ListView):
    model = ProxyList
    template_name = 'delete.html'


class DetailPageView(DetailView):
    model = ProxyList
    template_name = 'detail.html'
    context_object_name = 'proxy'
