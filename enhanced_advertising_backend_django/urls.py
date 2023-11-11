from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('ws/video_stream/', views.video_stream, name='video_stream'),
]
