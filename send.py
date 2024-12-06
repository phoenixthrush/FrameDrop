import time
import tkinter as tk


def display_binary_string(binary_string):
    def update_color():
        if index[0] < len(binary_string):
            bit = binary_string[index[0]]

            if bit == "0":
                print(f"{index[0]:02}: {bit}")
                root.configure(bg="black")
            else:
                print(f"{index[0]:02}: {bit}")
                root.configure(bg="white")

            index[0] += 1
            root.after(500, update_color)
        else:
            root.destroy()

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg="white")
    root.bind('<Escape>', lambda e: root.destroy())

    index = [0]
    update_color()

    root.mainloop()


x = "lol"
binary_string = ''.join(f"0{format(ord(char), 'b')}" for char in x)
print(binary_string)

time.sleep(1.5)
display_binary_string(binary_string)
