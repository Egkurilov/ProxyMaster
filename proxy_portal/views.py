from datetime import datetime

from django.forms import Textarea, DateTimeField
from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import ProxyList


class HomePageView(ListView):
    model = ProxyList
    template_name = 'index.html'
    context_object_name = 'all_proxy_list'


def login_view(request):
    if request.POST:
        form_data = request.POST.dict()
    date_now = datetime.now()
    formated_date = date_now.strftime("%d.%m.%Y %H:%M")

    return render(request, "add.html", {'formated_date': formated_date})

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
