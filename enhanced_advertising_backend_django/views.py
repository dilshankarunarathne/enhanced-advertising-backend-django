from django.http import JsonResponse
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt
import json

from enhanced_advertising_backend_django.stats import populate


def video_stream(request):
    return JsonResponse({"message": "Video stream placeholder"})


@csrf_exempt
def post_view(request):
    if request.method == 'POST':
        stat = populate()
        stat.pop('_id', None)
        return JsonResponse(stat)
