import time
import qrcode

with open('data/data.txt', 'r') as file:
    data = file.read().strip()

def display_qr_code(char):
    print(char, end="")

    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )

    qr.add_data(char)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

    time.sleep(3)

# Send metadata
display_qr_code(len(data))

for char in data:
    display_qr_code(char)
