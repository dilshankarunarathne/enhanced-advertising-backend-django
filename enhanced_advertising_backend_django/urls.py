from django.contrib import admin
from django.urls import path
from . import views, consumers
from django.urls import re_path
from .views import post_view, image_view

urlpatterns = [
    path('ws/video_stream/', views.video_stream, name='video_stream'),
    path('api/report', post_view),
    path('api/image', image_view),
]

websocket_urlpatterns = [
    re_path(r'ws/video_stream/$', consumers.VideoStreamConsumer),
]
