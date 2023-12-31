import asyncio
import json
import base64
import cv2
import numpy as np
import re

from channels.generic.websocket import AsyncWebsocketConsumer

from enhanced_advertising_backend_django import classifier
from enhanced_advertising_backend_django.ad_engine.main import get_ad_img_url
from enhanced_advertising_backend_django.iengine.recommender import predict_interest


class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Extract base64 string from data URL
        base64_str = re.search(r'base64,(.*)', text_data).group(1)
        frame_data = base64.b64decode(base64_str)
        nparr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if frame is None:
            print("error frame is none")
        else:
            print("Image decoded successfully")
        model_output = model_processing(frame)
        await self.send(text_data=json.dumps({"model_output": model_output}))



def check_base64_image(base64_string, output_file):
    try:
        with open(output_file, 'wb') as f_out:
            f_out.write(base64.b64decode(base64_string))
        print(f"Image written to {output_file}. Please check if it's a valid image.")
    except Exception as e:
        print(f"Failed to decode and write image: {e}")


def model_processing(frame):
    if frame is None:
        print("image empty")

    # predict age & gender
    age, gender = classifier.predict_age_and_gender(frame)

    # predict interest
    recommended_interest = predict_interest(age, gender)

    # get ad
    ad = get_ad_img_url(recommended_interest)

    return age, gender, recommended_interest, ad
