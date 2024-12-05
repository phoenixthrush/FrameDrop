import cv2
import time

camera = cv2.VideoCapture(0)

try:
    while True:
        time.sleep(1)
        ret, frame = camera.read()

        if ret:
            height, width, _ = frame.shape
            mid_pixel = frame[height // 2, width // 2]

            print()
            print(mid_pixel[0])  # B
            print(mid_pixel[1])  # G
            print(mid_pixel[2])  # R

            if mid_pixel[0] < 128 and mid_pixel[1] < 128 and mid_pixel[2] < 128:
                print("Black")
            else:
                print("White")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    camera.release()
    cv2.destroyAllWindows()
