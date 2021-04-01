from django.urls import path
from .views import HomePageView, login_view, DelPageView, EditView, DetailPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add/', login_view, name='add'),
    path('proxy/<int:pk>/', DetailPageView.as_view(), name='proxy_detail'),
    path('del/', DelPageView.as_view(), name='del'),
    path('edit/', EditView.as_view(), name='edit'),
]
