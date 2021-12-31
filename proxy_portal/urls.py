from django.urls import path

from .utils import check_all_proxy_status
from .views import HomePageView, DelPageView, start_proxy, stop_proxy, edit_proxy, add_project_view, add_entry_view, \
    edit_save, proxy_status, json_view

urlpatterns = [
    # main route
    path('', HomePageView.as_view(), name='home'),
    path('add_entry/', add_entry_view, name='add_entry_view'),
    path('add_project/', add_project_view, name='add_project_view'),
    # route for control proxy
    path('start/<int:pk>/', start_proxy, name='start_proxy'),
    path('stop/<int:pk>/', stop_proxy, name='stop_proxy'),
    path('edit/<int:pk>/', edit_proxy, name='edit_proxy'),
    path('edit_save/', edit_save, name='edit_save'),
    path('start/<int:pk>/', start_proxy, name='start_proxy'),

    path('check_all_proxy_status/', check_all_proxy_status, name='check_all_proxy_status'),
    # route add/del
    path('del/', DelPageView.as_view(), name='del'),

    path('json/', json_view, name='json_view'),
]
