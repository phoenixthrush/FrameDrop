import time
import json

from cv2 import VideoCapture
from pyzbar.pyzbar import decode

cam = VideoCapture(0)


def scan():
    _, image = cam.read()
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            return obj.data.decode('utf-8')

    return '?'


def receive_data():
    metadata_json = scan()
    metadata = json.loads(metadata_json)

    print(metadata)

    FILE_NAME = metadata["file_name"]
    # DATA_SIZE = metadata["data_size"]
    # CHUNK_SIZE = metadata["chunk_size"]
    CHUNK_COUNT = metadata["chunk_count"]
    TIME_SEEP = metadata["time_sleep"]

    time.sleep(TIME_SEEP)

    with open(FILE_NAME, 'wb') as file:
        for _ in range(CHUNK_COUNT):
            chunk_data = scan()
            file.write(chunk_data.encode('utf-8'))
            time.sleep(TIME_SEEP)

    cam.release()


if __name__ == '__main__':
    receive_data()
