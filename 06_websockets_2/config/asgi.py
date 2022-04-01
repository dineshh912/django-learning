"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifier.consumers import EchoConsumer, TickTockConsumer,UserCreatedConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", EchoConsumer()),
        path("ws/tick/", TickTockConsumer()),
        path("ws/notification/", UserCreatedConsumer.as_asgi())
    ])
})