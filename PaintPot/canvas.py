from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

global value
value = "red"

window = Tk()

def change(n):

    if n == 0:
        value = "red"
    elif n == 1:
        value = "blue"
        print("blue")
    else:
        value = "green"

window.geometry('305x400')

canvas = Canvas(window, width = 300, height = 300)
image = ImageTk.PhotoImage(file = "Originals/purr.png")
canvas.create_image(5, 5, image = image, anchor = NW)
canvas.grid(column = 0, row = 1)

check = Button(window, text="red", bg = "red", command = change(0)).grid(column = 0, row = 0, sticky = W)
check1 = Button(window, text="blue", bg = "blue", command = change(1)).grid(column = 0, row = 0, sticky = N)
check2 = Button(window, text="green", bg = "green", command = change(2)).grid(column = 0, row = 0, sticky = E)


Label = Label(window, text="Tamany del Llpais: ").grid(column = 0, row = 2, sticky = W)
clear = Button(window, text="Restarteja").grid(column = 0, row = 2, sticky = E)


combo1 = ttk.Combobox(window, state="readonly", width=10)
combo1["values"] = ["2", "3", "4", "5"]
combo1.set("2")

combo1.grid(column = 0, row = 2)

def click(event):    
    x, y = event.x, event.y
    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
    size = combo1.get()
    canvas.create_oval( [x1+2, y1+2, x2, y2], outline='%s' % value, width = size, dash = (100,))
       
canvas.bind("<B1-Motion>", click)

window.mainloop()
