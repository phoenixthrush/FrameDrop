import time
import json

import qrcode


def display_qr_code(data):
    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

    time.sleep(3)


def send_data():
    with open('data/data.txt', 'r') as file:
        data = file.read().strip()

    DATA_SIZE = len(data)
    CHUNK_SIZE = 1024
    TIME_SLEEP = 3

    METADATA = json.dumps({
        "filename": "data.txt",
        "data_size": DATA_SIZE,
        "chunk_size": CHUNK_SIZE,
        "chunk_count": (DATA_SIZE + CHUNK_SIZE - 1) // CHUNK_SIZE,
        "time_sleep": TIME_SLEEP
    })

    print(METADATA)
    display_qr_code(METADATA)

    for i in range(0, len(data), CHUNK_SIZE):
        chunk = data[i:i+CHUNK_SIZE]
        display_qr_code(chunk)


if __name__ == "__main__":
    send_data()
