from tkinter import *
from tkinter import ttk

window = Tk()

window.geometry('305x400')

canvas = Canvas(window, width = 300, height = 300, bg = "white")
canvas.grid(column = 0, row = 1)

combo = ttk.Combobox(window, state="readonly")
combo["values"] = ["black", "blue", "yellow", "green"]
combo.set("black")

combo1 = ttk.Combobox(window, state="readonly")
combo1["values"] = ["2", "2.5", "3", "4"]
combo1.set("2")

combo.grid(column = 0, row = 0, sticky = W)
combo1.grid(column = 0, row = 0, sticky = E)

def click(event):    
    x, y = event.x, event.y
    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
    value = combo.get()
    size = combo1.get()
    canvas.create_rectangle( [x1+2, y1+2, x2, y2], outline='%s' % value, width = size, dash = (100,))
       
canvas.bind("<B1-Motion>", click)

window.mainloop()
