import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from enhanced_advertising_backend_django import consumers
from enhanced_advertising_backend_django.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enhanced_advertising_backend_django.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path('ws/video_stream/', consumers.VideoStreamConsumer),
    ]),
})
