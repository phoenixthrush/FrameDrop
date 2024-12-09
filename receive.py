import cv2
import time

FREQ = 2

camera = cv2.VideoCapture(0)

if time.localtime().tm_sec % 10 > 7:
    time.sleep(3)

while time.localtime().tm_sec % 10 != 0:
    time.sleep(0.1)

try:
    binary_array_bit_length = []

    if binary_array_bit_length:
        _binary_string = ''.join(map(str, binary_array_bit_length))
        bit_length = int(_binary_string, 2)
    else:
        bit_length = 0

    binary_array = []

    for i in range(4):
        while time.localtime().tm_sec % FREQ != 0:
            time.sleep(0.05)
        ret, frame = camera.read()
        if ret:
            height, width, _ = frame.shape
            mid_pixel = frame[height // 2, width // 2]

            if mid_pixel[0] >= 128 or mid_pixel[1] >= 128 or mid_pixel[2] >= 128:
                binary_value = 1
            else:
                binary_value = 0

            print(f"{time.time()} {i:02}: {binary_value}")
            binary_array.append(binary_value)

            next_full_second = ((time.localtime().tm_sec // FREQ) + 1) * FREQ
            now = time.localtime().tm_sec
            time.sleep(max(0, next_full_second - now - 0.05))

    if binary_array:
        _binary_string = ''.join(map(str, binary_array))
        bit_length = int(_binary_string, 2)
    else:
        bit_length = 0

    print(bit_length)

    binary_array = []

    for i in range(bit_length * 8):
        while time.localtime().tm_sec % FREQ != 0:
            time.sleep(0.05)
        ret, frame = camera.read()
        if ret:
            height, width, _ = frame.shape
            mid_pixel = frame[height // 2, width // 2]

            if mid_pixel[0] >= 128 or mid_pixel[1] >= 128 or mid_pixel[2] >= 128:
                binary_value = 1
            else:
                binary_value = 0

            print(f"{time.time()} {i:02}: {binary_value}")
            binary_array.append(binary_value)

            next_full_second = ((time.localtime().tm_sec // FREQ) + 1) * FREQ
            now = time.localtime().tm_sec
            time.sleep(max(0, next_full_second - now - 0.05))

    binary_string = ''.join(map(str, binary_array))

    while len(binary_string) % 8 != 0:
        binary_string = '0' + binary_string

    if binary_string:
        decimal_value = int(binary_string, 2)
        byte_count = (decimal_value.bit_length() + 7) // 8
        byte_value = decimal_value.to_bytes(byte_count, 'big')

        print(f"Binary String: {binary_string}")
        print(f"Decimal Value: {decimal_value}")
        print(f"Byte Value: {byte_value}")

        utf8_text = byte_value.decode('utf-8', errors='ignore')
        print(f"Decoded Text: {utf8_text}")
    else:
        print("Binary string is empty; no values were captured.")
except KeyboardInterrupt:
    pass
finally:
    camera.release()
    cv2.destroyAllWindows()
