from pyzbar.pyzbar import decode
from PIL import Image
from cv2 import VideoCapture


cam = VideoCapture(0)
_, image = cam.read() 

decoded_objects = decode(image)
for obj in decoded_objects:
    print(f"Data: {obj.data.decode('utf-8')}")