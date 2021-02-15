import pyqrcode
from tkinter import *
from PIL import ImageTk, Image
import time

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
data = input("Enter the link/data:")
code = pyqrcode.create(data)
img = code.png(f'qrcode{round(time.time())}.png', scale=8)
img_to_display = ImageTk.PhotoImage(Image.open(f"qrcode{round(time.time())}.png"))
canvas.create_image(40, 40, anchor=NW, image=img_to_display)
root.mainloop()
