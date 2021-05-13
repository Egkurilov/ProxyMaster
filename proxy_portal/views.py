from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.views.generic import ListView, DetailView
from .utils import proxy_run, proxy_kill
from .models import ProxyList, ProjectList


class HomePageView(ListView):
    model = ProxyList
    template_name = 'index.html'
    context_object_name = 'all_proxy_list'
    queryset = ProxyList.objects.all()
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        project_list = ProjectList.objects.values('id', 'project_name').all
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['project_list'] = project_list
        return context


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
        project_name = request.POST.get('project_name_input')
        proxy_name = request.POST.get('proxy_name_input')
        fp_name = request.POST.get('fp_name_input')
        proxy_port_out = request.POST.get('proxy_port_out_input')
        stop_date = request.POST.get('stop_date_input')
        start_date = request.POST.get('start_date_input')

        query_result = ProxyList.objects.latest('proxy_port_in').proxy_port_in

        ProxyList.objects.create(
            project_id=project_name,
            proxy_name=proxy_name,
            fp_name=fp_name,
            proxy_port_in=query_result+1,
            proxy_port_out=proxy_port_out,
            stop_date=datetime.strptime(stop_date, '%d.%m.%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S.000000'),
            start_date=datetime.strptime(start_date, '%d.%m.%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S.000000'),
        )
    return redirect('home')


def add_project_view(request):
    if request.POST:
        new_project = request.POST.get('project_name')
        if new_project is not None:
            ProjectList.objects.create(project_name=new_project)

        print("POST add_project_view")
    return redirect('home')


class DelPageView(ListView):
    model = ProxyList
    template_name = 'delete.html'


class DetailPageView(DetailView):
    model = ProxyList
    template_name = 'detail.html'
    context_object_name = 'proxy'
