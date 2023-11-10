import asyncio
import json
import base64
import cv2
import numpy as np

from channels.generic.websocket import AsyncWebsocketConsumer


class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Decode the base64-encoded video frame
        frame_data = base64.b64decode(text_data)

        # Convert the frame data to a NumPy array
        nparr = np.frombuffer(frame_data, np.uint8)

        # Decode the image
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Perform image processing with your OpenCV model
        processed_frame = your_opencv_model_processing(frame)

        # Encode the processed frame as JPEG
        _, encoded_frame = cv2.imencode('.jpg', processed_frame)

        # Convert the encoded frame to base64
        base64_encoded_frame = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

        # Send the processed frame back to the client
        await self.send(text_data=json.dumps({'frame': base64_encoded_frame}))


def your_opencv_model_processing(frame):
    # Implement your OpenCV model processing logic here
    # For example, you can apply object detection, facial recognition, etc.
    # Make sure to return the processed frame
    return frame
