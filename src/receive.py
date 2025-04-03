from pyzbar.pyzbar import decode
from cv2 import VideoCapture

cam = VideoCapture(0)
_, image = cam.read() 

decoded_objects = decode(image)

if decoded_objects:
    for obj in decoded_objects:
        print(f"Data: {obj.data.decode('utf-8')}")
else:
    print("No QR Code found")
