from datetime import datetime

from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import randrange
# Create your views here.
from django.template import loader
from django.views.generic import ListView, DetailView
from .utils import proxy_run, proxy_kill
from .models import ProxyList


class HomePageView(ListView):
    model = ProxyList
    template_name = 'index.html'

    context_object_name = 'all_proxy_list'

def main_view(request):
    proxylist = ProxyList()
    if request.POST:
        print(ProxyList.objects.aggregate(Max('proxy_port_in')))
        proxylist.save()
    date_now = datetime.now()
    formated_date = date_now.strftime("%Y.%m.%d %H:%M")

    return render(request, "add_entry.html", {'formated_date': formated_date})


def start_proxy(request, pk):
    query_result = ProxyList.objects.values().filter(id=pk)
    pid = proxy_run(str(query_result[0]['proxy_port_in']), str(query_result[0]['proxy_port_out']))
    ProxyList.objects.values().filter(id=pk).update(proxy_pid=pid)
    ProxyList.objects.values().filter(id=pk).update(status=True)

    return redirect('home')


def stop_proxy(request, pk):
    query_result = ProxyList.objects.values('proxy_pid').filter(id=pk)
    proxy_kill(str(query_result[0]['proxy_pid']))

    ProxyList.objects.values().filter(id=pk).update(proxy_pid=0, status=False)
    # ProxyList.objects.filter(id=pk).update(status=False)
    return redirect('home')


def edit_proxy(request, pk):
    if request.POST:
        print("POST")
    query_result = ProxyList.objects.filter(id=pk)
    template = loader.get_template('edit.html')
    context = {
        'query_result': query_result,
    }
    return HttpResponse(template.render(context))


def add_entry_view(request):
    if request.POST:
        print("POST")
    return redirect('home')


def add_project_view(request):
    if request.POST:
        print("POST")
    return redirect('home')


class DelPageView(ListView):
    model = ProxyList
    template_name = 'delete.html'


class DetailPageView(DetailView):
    model = ProxyList
    template_name = 'detail.html'
    context_object_name = 'proxy'
