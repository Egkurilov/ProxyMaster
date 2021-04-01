import os
import subprocess

# prc = subprocess.call(['proxy', 'http', '-t', 'tcp', '-p', '"0.0.0.0:38080"'],stderr=subprocess.STDOUT , shell=True)

customp_port = "0.0.0.0:37300"
stream = os.popen(f'nohup proxy http -t tcp -p {customp_port} --daemon &')
output = stream.read()

print(output)
