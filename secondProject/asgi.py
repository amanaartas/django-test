"""
ASGI config for clinicProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import secondProject.secondApp.routing

# from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secondProject.settings')
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        secondProject.secondApp.routing.websocket_urlpatterns
    )
})
 

