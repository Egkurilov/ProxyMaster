import codecs
import subprocess
import re


# prc = subprocess.call(['proxy', 'http', '-t', 'tcp', '-p', '"0.0.0.0:38080"'],stderr=subprocess.STDOUT , shell=True)

# customp_port = "0.0.0.0:37300"
# commands = ['proxy', 'http', '-t', 'tcp', '-p', ":37300", '-P', "0.0.0.0:38080", '--daemon', '--forever']

# process = subprocess.run(['sh', './start_proxy.sh', '37300', '38080', 'project_name'],
# cwd='../pfiles')
# proxy http -t tcp -p ":37300" -P "0.0.0.0:38080" --daemon --forever
# com_string = ['proxy', 'http', '-t', 'tcp', '-p', ":37300", '-P', "0.0.0.0:38080", '--daemon', '--forever']
# coms_string = 'proxy http -T tcp -p :32000 -P "0.0.0.0:32000" --daemon --forever construing'
from django.http import JsonResponse

from proxy_portal.models import ProxyList


def proxy_run(port_in, port_out):
    command = ['./start_proxy.sh', port_out, port_in]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd='/home/shaneque/PycharmProjects/ProxyMaster/pfiles')
    command_output = proc.stdout.read().decode("utf-8")
    pid = re.search('\[PID\] (\d+) running', command_output).group(1)
    return pid


def proxy_kill(pid):
    command = ['kill', '-9', pid]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.wait()
    return True


def check_proxy(pid):
    command = ['./check_proxy.sh', pid]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd='/home/shaneque/PycharmProjects/ProxyMaster/pfiles')
    process.wait()
    return process.stdout.read()


def proxy_status(pid):
    status = check_proxy(pid)
    if status is b'':
        return False

    return True


def check_all_proxy_status(request):
    query_status = ProxyList.objects.values('id', 'proxy_pid').exclude(proxy_pid=0)
    for status in query_status:
        actual_status = proxy_status(str(status['proxy_pid']))
        if actual_status is False:
            ProxyList.objects.values().filter(id=status['id']).update(status=False)
    return JsonResponse({"status": True}, status=200)
