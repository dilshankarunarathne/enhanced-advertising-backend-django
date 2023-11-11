import asyncio
import json
import base64
import cv2
import numpy as np

from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings

default_channel_layer = settings.DEFAULT_CHANNEL_LAYER


class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        frame_data = base64.b64decode(text_data)
        nparr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        processed_frame = model_processing(frame)
        _, encoded_frame = cv2.imencode('.jpg', processed_frame)
        base64_encoded_frame = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')
        model_output = model_processing(processed_frame)  
        await self.send(text_data=json.dumps({'frame': base64_encoded_frame, 'model_output': model_output}))


def model_processing(frame):
    # Implement your OpenCV model processing logic here
    # For example, you can apply object detection, facial recognition, etc.
    # TODO Make sure to return the processed frame
    return "data comes in..."
