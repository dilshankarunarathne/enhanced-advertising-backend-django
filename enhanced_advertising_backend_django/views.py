from django.http import JsonResponse
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt
import json


def video_stream(request):
    return JsonResponse({"message": "Video stream placeholder"})


@csrf_exempt
def post_view(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        # process data
        # return response
        return JsonResponse({'message': 'Data received'})
