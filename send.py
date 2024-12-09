import time
import tkinter as tk

FREQ = 2


def display_binary_string(binary_string):
    def update_color():
        print(time.time())
        if index[0] < len(binary_string):
            bit = binary_string[index[0]]

            if bit == "0":
                print(f"{index[0]:02}: {bit}")
                root.configure(bg="black")
            else:
                print(f"{index[0]:02}: {bit}")
                root.configure(bg="white")

            index[0] += 1

            now = time.time()
            next_tick = (int(now // FREQ) + 1) * FREQ
            delay = max(0, int((next_tick - now) * 1000))
            root.after(delay, update_color)

        else:
            root.destroy()

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg="white")
    root.bind('<Escape>', lambda e: root.destroy())

    index = [0]
    update_color()

    root.mainloop()


string = "lol"
string_bin = ''.join(f"0{format(ord(char), 'b')}" for char in string)

length_bin = bin(len(string)).replace("0b", "").zfill(4)

wow = length_bin + string_bin

if time.localtime().tm_sec % 10 > 7:
    time.sleep(3)

while time.localtime().tm_sec % 10 != 0:
    time.sleep(0.1)

display_binary_string(wow)
