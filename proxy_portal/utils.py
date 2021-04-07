import os
import subprocess

# prc = subprocess.call(['proxy', 'http', '-t', 'tcp', '-p', '"0.0.0.0:38080"'],stderr=subprocess.STDOUT , shell=True)

customp_port = "0.0.0.0:37300"
commands = ['proxy', 'http', '-t', 'tcp', '-p', ":37300", '-P', "0.0.0.0:38080", '--daemon', '--forever']

process = subprocess.run(['sh', './start_proxy.sh', '37300', '38080', 'project_name'],
                           cwd='../pfiles')


print(process)
#proxy http -t tcp -p ":37300" -P "0.0.0.0:38080" --daemon --forever