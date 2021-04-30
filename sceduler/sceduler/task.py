import time

from proxy_portal.models import ProxyList

while True:
    query_result = ProxyList.objects.values().filter()
    print(query_result)
    time.sleep(10)