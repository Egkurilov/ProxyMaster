import time
from datetime import datetime
from proxy_portal.models import ProxyList
from proxy_portal.views import start_proxy, stop_proxy


def pr():
    while True:
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M")

        query_result = ProxyList.objects.values('id', 'start_date', 'stop_date', 'proxy_id')
        for single_q in query_result:
            if str(single_q['start_date'])[:-3] == datetime_now:
                print("str(single_q['start_date'])[:-3], '==', datetime_now")
            if str(single_q['stop_date'])[:-3] == datetime_now:
                print("str(single_q['stop_date'])[:-3] == datetime_now")

        time.sleep(60)
