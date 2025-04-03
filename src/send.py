import time
import json

import qrcode


def display_qr_code(data):
    """
    QR Code Error Correction Levels:
        - ERROR_CORRECT_L: About 07% or less
        - ERROR_CORRECT_M: About 15% or less (default)
        - ERROR_CORRECT_Q: About 25% or less
        - ERROR_CORRECT_H: About 30% or less
    """

    qr = qrcode.QRCode(
        version=25,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

    time.sleep(3)


def send_data():
    FILE = "IMG_1077.jpeg"

    with open(f'data/{FILE}', 'r') as file:
        data = file.read().strip()

    DATA_SIZE = len(data)
    CHUNK_SIZE = 2048
    TIME_SLEEP = 3

    METADATA = json.dumps({
        "filename": FILE,
        "data_size": DATA_SIZE,
        "chunk_size": CHUNK_SIZE,
        "chunk_count": (DATA_SIZE + CHUNK_SIZE - 1) // CHUNK_SIZE,
        "time_sleep": TIME_SLEEP
    })

    print(json.dumps(json.loads(METADATA), indent=4))
    display_qr_code(METADATA)

    for i in range(0, len(data), CHUNK_SIZE):
        chunk = data[i:i+CHUNK_SIZE]
        display_qr_code(chunk)


if __name__ == "__main__":
    send_data()
