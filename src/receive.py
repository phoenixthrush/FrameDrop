from pyzbar.pyzbar import decode
from cv2 import VideoCapture
import time
import sys

CHUNK_COUNT = 5

cam = VideoCapture(0)


def scan():
    _, image = cam.read()

    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            return (obj.data.decode('utf-8'))

    return ("No QR Code found\n")


for i in range(CHUNK_COUNT):
    char = scan()

    print(char, end="")
    sys.stdout.flush()

    time.sleep(3)

cam.release()
