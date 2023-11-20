from django.http import JsonResponse
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt
import json

from enhanced_advertising_backend_django.mongo import put_image
from enhanced_advertising_backend_django.stats import populate, populate_with_month, get_month


def video_stream(request):
    return JsonResponse({"message": "Video stream placeholder"})


@csrf_exempt
def post_view(request):
    if request.method == "GET":
        month = request.GET.get('month', get_month())
        stat = populate_with_month(month)
        stat.pop('_id', None)
        return JsonResponse(stat)

    elif request.method == 'POST':
        stat = populate()
        stat.pop('_id', None)
        return JsonResponse(stat)


@csrf_exempt
def image_view(request):
    if request.method == "POST":
        image = request.FILES['image']
        name = request.POST['name']

        filename = name + ".jpg"
        image_id = put_image(filename, image)
        
        return JsonResponse({"image_id": image_id})
