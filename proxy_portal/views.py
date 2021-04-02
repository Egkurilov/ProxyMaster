from datetime import datetime

from django.db.models import Max
from django.forms import Textarea, DateTimeField
from django.http import HttpResponse, request
from django.shortcuts import render
from random import randrange
# Create your views here.
from django.views.generic import ListView, DetailView

from . import models
from .models import ProxyList


class HomePageView(ListView):
    model = ProxyList
    template_name = 'index.html'
    context_object_name = 'all_proxy_list'


def login_view(request):
    proxylist = ProxyList()
    if request.POST:
        # form_data = request.POST.dict()
        # proxylist.id = models.ProxyList.objects.latest('id').id
        # proxylist.start_date = request.POST.get('form_data')
        # proxylist.stop_date = request.POST.get('form_data')
        proxylist.proxy_id = 1
        proxylist.project_id = 1
        proxylist.proxy_port_in = 1
        proxylist.proxy_port_out = 1
        proxylist.proxy_name = 5
        proxylist.fp_name = 4
        proxylist.author = 3
        proxylist.stop_date = request.POST.get('form_data')
        proxylist.start_date = request.POST.get('form_data')
        proxylist.status = 1
        print(ProxyList.objects.aggregate(Max('proxy_port_in')))
        proxylist.save()
    date_now = datetime.now()
    formated_date = date_now.strftime("%Y.%m.%d %H:%M")

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
