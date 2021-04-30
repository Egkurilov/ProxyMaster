import subprocess
import re



# prc = subprocess.call(['proxy', 'http', '-t', 'tcp', '-p', '"0.0.0.0:38080"'],stderr=subprocess.STDOUT , shell=True
# customp_port = "0.0.0.0:37300"
# commands = ['proxy', 'http', '-t', 'tcp', '-p', ":37300", '-P', "0.0.0.0:38080", '--daemon', '--forever']
# process = subprocess.run(['sh', './start_proxy.sh', '37300', '38080', 'project_name'],
# cwd='../pfiles')
# proxy http -t tcp -p ":37300" -P "0.0.0.0:38080" --daemon --forever
# com_string = ['proxy', 'http', '-t', 'tcp', '-p', ":37300", '-P', "0.0.0.0:38080", '--daemon', '--forever']
# coms_string = 'proxy http -T tcp -p :32000 -P "0.0.0.0:32000" --daemon --forever construing'


def proxy_run(port_in, port_out):
    command = ['./proxy', 'http', '-t', 'tcp', '-p', '"'+port_in+'"', '-P', '":'+port_out+'"', '--daemon', '--forever']
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd='../pfiles')
    command_output = proc.stdout.read().decode("utf-8")
    pid = re.search('\[PID\] (\d+) running', command_output).group(1)
    return pid


def proxy_kill(pid):
    command = ['kill', '-9', pid]
    subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return True


