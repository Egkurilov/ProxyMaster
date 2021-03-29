from django.contrib import admin

# Register your models here.
from .models import ProxyList, ProjectList

admin.site.register(ProxyList)
admin.site.register(ProjectList)
