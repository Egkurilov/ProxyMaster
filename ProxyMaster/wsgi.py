"""
WSGI config for ProxyMaster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import threading
from proxy_portal.sceduler import pr
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProxyMaster.settings')

application = get_wsgi_application()

x = threading.Thread(target=pr)
x.start()