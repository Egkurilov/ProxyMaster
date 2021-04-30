import time

from django.apps import AppConfig

#from proxy_portal.sceduler import search_task


class ProxyPortalConfig(AppConfig):
    name = 'proxy_portal'

    # while True:
    #     search_task()
    #     time.sleep(10)
