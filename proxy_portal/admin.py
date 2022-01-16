from django.contrib import admin

# Register your models here.
from .models import ProxyList, ProjectList, ProxySettings


class PLAdmin(admin.ModelAdmin):
    list_display = ('proxy_port_in', 'project', 'proxy_name', 'status')
    list_filter = ('project', 'status')
 

class PjAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name')


class PsAdmin(admin.ModelAdmin):
    list_display = ('id', 'proxy_name', 'proxy_value')


admin.site.register(ProxyList, PLAdmin)
admin.site.register(ProjectList, PjAdmin)
admin.site.register(ProxySettings, PsAdmin)
