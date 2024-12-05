import tkinter as tk


def display_binary_string(binary_string):
    def update_color():
        nonlocal index
        if index < len(binary_string):
            bit = binary_string[index]
            root.configure(bg="black" if bit == "0" else "white")
            index += 1
            root.after(500, update_color)
        else:
            root.destroy()

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg="white")
    root.bind('<Escape>', lambda e: root.destroy())

    index = 0
    update_color()

    root.mainloop()


x = "hello"
binary_string = ''.join(f"0{format(ord(char), 'b')}" for char in x)


display_binary_string(binary_string)
