import base64
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
import io


# Create your views here.


def encode_image_to_base64(image_path):
    # Open the image using Pillow
    with Image.open(image_path) as img:
        # Create a BytesIO buffer to hold the image data in memory
        buffered = BytesIO()
        # Save the image to the buffer as a PNG (or any other format)
        img.save(buffered, format="PNG")
        # Get the byte data from the buffer
        img_bytes = buffered.getvalue()
        # Encode the byte data to base64
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        return img_base64

def teszt(request):
    # Load an image
    #image = encode_image_to_base64('teszt/testImage/20180718_114351-1.JPG')
    image = Image.open('teszt/testImage/20180718_114351-1.JPG')
    buffer = io.BytesIO()


    # Save the image to the buffer in a desired format (e.g., JPEG)
    image.save(buffer, format='JPEG')
    buffer.seek(0)  # Move the cursor to the start of the BytesIO buffer

    # Create an HttpResponse with the image data
    response = HttpResponse(buffer, content_type='image/jpeg')
    response['Content-Disposition'] = 'inline; filename="image.jpg"'

    return response
