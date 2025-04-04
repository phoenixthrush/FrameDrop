import base64
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
    METADATA = scan()
    METADATA_JSON = json.loads(METADATA)

    print(json.dumps(json.loads(METADATA), indent=4))

    FILE_NAME = METADATA_JSON["filename"]
    # DATA_SIZE = METADATA_JSON["data_size"]
    # CHUNK_SIZE = METADATA_JSON["chunk_size"]
    CHUNK_COUNT = METADATA_JSON["chunk_count"]
    TIME_SEEP = METADATA_JSON["time_sleep"]

    time.sleep(TIME_SEEP)

    with open(FILE_NAME, 'wb') as file:
        for i in range(CHUNK_COUNT):
            print(f"Progress: {i}/{CHUNK_COUNT}")
            chunk_data = scan()
            decoded_data = base64.b64decode(chunk_data)
            file.write(decoded_data)
            time.sleep(TIME_SEEP)

    cam.release()


if __name__ == '__main__':
    try:
        receive_data()
    except KeyboardInterrupt:
        pass
