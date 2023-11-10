from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from enhanced_advertising_backend_django.src.consumers import VideoConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/video/", VideoConsumer.as_asgi()),
    ]),
})
