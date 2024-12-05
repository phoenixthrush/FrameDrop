import cv2
import time

BIT_LENGHT = 24  # TODO - fetch this on calibrate

camera = cv2.VideoCapture(0)

try:
    # contains "lol"
    # binary_array = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0]

    binary_array = []

    for i in range(BIT_LENGHT):
        time.sleep(0.5)
        ret, frame = camera.read()
        if ret:
            height, width, _ = frame.shape
            mid_pixel = frame[height // 2, width // 2]

            if mid_pixel[0] >= 128 or mid_pixel[1] >= 128 or mid_pixel[2] >= 128:
                binary_value = 1
            else:
                binary_value = 0

            print(f"{i:02}: {binary_value}")
            binary_array.append(binary_value)

    binary_string = ''.join(map(str, binary_array))
    decimal_value = int(binary_string, 2)
    byte_value = decimal_value.to_bytes(len(binary_string) // 8, 'big')
    utf8_text = byte_value.decode('utf-8', errors='ignore')

    print(utf8_text)
except KeyboardInterrupt:
    pass
finally:
    camera.release()
    cv2.destroyAllWindows()
