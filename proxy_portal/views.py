import json
import time
from datetime import datetime

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.views.generic import ListView, DetailView
from .utils import proxy_run, proxy_kill, check_proxy, proxy_status, check_all_proxy_status
from .models import ProxyList, ProjectList
from django.views.decorators.csrf import csrf_exempt


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


def json_view(request):
    dict = {}
    dict['data'] = []
    qs = ProxyList.objects.filter().values('proxy_port_in', 'proxy_name', 'project__project_name', \
                                           'proxy_port_out', 'stop_date', 'start_date', 'status', 'id')

    for q in qs:
        proxy_id = q['id']
        dict['data'].append([q['proxy_port_in'],
                             q['proxy_name'],
                             q['project__project_name'],
                             q['proxy_port_out'],
                             q['stop_date'].strftime("%d.%m.%Y %H:%M"),
                             q['start_date'].strftime("%d.%m.%Y %H:%M"),
                             q['status'],
                             f"""                <div class="btn-group" role="group">
                    <a href="javascript:void(0)" data-id="{proxy_id}" class="btn-sm btn btn-success start-proxy"  role="button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
                            <path d="M11.596 8.697l-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>
                        </svg>
                    </a>
                    <a href="/edit/{proxy_id}" class="btn-sm btn btn-warning" role="button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
                            <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
                        </svg>
                    </a>
                    <a href="javascript:void(0)" data-id="{proxy_id}" class="btn-sm btn btn-danger stop-proxy" role="button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stop-fill" viewBox="0 0 16 16">
                            <path d="M5 3.5h6A1.5 1.5 0 0 1 12.5 5v6a1.5 1.5 0 0 1-1.5 1.5H5A1.5 1.5 0 0 1 3.5 11V5A1.5 1.5 0 0 1 5 3.5z"/>
                        </svg>
                    </a>
                </div>""".format(proxy_id=proxy_id)])

    return JsonResponse(dict, status=200)


def start_proxy(request, pk):
    query_status = ProxyList.objects.values('status').filter(id=pk)
    for status in query_status:
        if status['status'] is not True:
            query_result = ProxyList.objects.values().filter(id=pk)
            pid = proxy_run(str(query_result[0]['proxy_port_in']), str(query_result[0]['proxy_port_out']))
            if pid is not None:
                ProxyList.objects.values().filter(id=pk).update(proxy_pid=pid)
                ProxyList.objects.values().filter(id=pk).update(status=True)

                return JsonResponse({"status": proxy_status(pid)}, status=200)
        else:
            return redirect('home')


def stop_proxy(request, pk):
    query_status = ProxyList.objects.values('status').filter(id=pk)
    for status in query_status:
        if status['status'] is False:
            return redirect('home')
    query_result = ProxyList.objects.values('proxy_pid').filter(id=pk)
    proxy_kill(str(query_result[0]['proxy_pid']))
    ProxyList.objects.values().filter(id=pk).update(proxy_pid=0, status=False)
    return JsonResponse({"status": True}, status=200)


def edit_proxy(request, pk):
    if request.POST:
        print("POST")
    query_result = ProxyList.objects.filter(id=pk)
    template = loader.get_template('edit.html')
    context = {
        'query_result': query_result,
    }
    return HttpResponse(template.render(context))


@csrf_exempt
def edit_save(request):
    if request.POST:
        proxy_id = request.POST.get('proxy_id_input')
        stop_date = request.POST.get('stop_date_input')
        start_date = request.POST.get('start_date_input')

        ProxyList.objects.values().filter(id=proxy_id).update(
            proxy_name=request.POST.get('proxy_name_input'),
            proxy_port_out=request.POST.get('proxy_port_out_input'),
            stop_date=datetime.strptime(stop_date, '%d.%m.%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S.000000'),
            start_date=datetime.strptime(start_date, '%d.%m.%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S.000000'), )
    return redirect('home')


def add_entry_view(request):
    if request.POST:
        project_name = request.POST.get('project_name_input')
        proxy_name = request.POST.get('proxy_name_input')
        proxy_port_out = request.POST.get('proxy_port_out_input')
        stop_date = request.POST.get('stop_date_input')
        start_date = request.POST.get('start_date_input')

        try:
            last_port = ProxyList.objects.latest('proxy_port_in').proxy_port_in
        except ObjectDoesNotExist:
            last_port = 32000

        ProxyList.objects.create(
            project_id=project_name,
            proxy_name=proxy_name,
            proxy_port_in=last_port + 1,
            proxy_port_out=proxy_port_out,
            stop_date=datetime.strptime(stop_date, '%d.%m.%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S.000000'),
            start_date=datetime.strptime(start_date, '%d.%m.%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S.000000'),
        )
    return redirect('home')


# view для добавления нового проекта
def add_project_view(request):
    if request.POST:
        new_project = request.POST.get('project_name')
        if new_project is not None:
            if new_project != 'CARDS':
                ProjectList.objects.create(project_name=new_project)
    return redirect('home')


# Страница с заделом на будущее
class DelPageView(ListView):
    model = ProxyList
    template_name = 'delete.html'


# Страница с заделом на будущее
class DetailPageView(DetailView):
    model = ProxyList
    template_name = 'detail.html'
    context_object_name = 'proxy'
