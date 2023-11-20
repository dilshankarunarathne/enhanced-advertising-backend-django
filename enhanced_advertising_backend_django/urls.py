from django.contrib import admin
from django.urls import path
from . import views, consumers
from django.urls import re_path
from .views import post_view

urlpatterns = [
    path('ws/video_stream/', views.video_stream, name='video_stream'),
    path('api/test', post_view),
]

websocket_urlpatterns = [
    re_path(r'ws/video_stream/$', consumers.VideoStreamConsumer),
    # re_path(r'ws/post-endpoint/$', consumers.PostConsumer.as_asgi()),
]
