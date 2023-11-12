import asyncio
import json
import base64
import cv2
import numpy as np

from channels.generic.websocket import AsyncWebsocketConsumer

from enhanced_advertising_backend_django.ad_engine.main import get_ad_img_url


class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        frame_data = base64.b64decode(text_data)
        nparr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        model_output = model_processing(frame)
        await self.send(text_data=json.dumps({model_output}))


def model_processing(frame):
    # predict age & gender
    age, gender = classifier.predict_age_and_gender(frame)

    # predict interest
    recommended_interest = predict_interest(age, gender)

    # get ad
    ad = get_ad_img_url(recommended_interest)

    return age, gender, recommended_interest, ad
