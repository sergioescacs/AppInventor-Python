from tkinter import *
from PIL import ImageTk,Image
from playsound import playsound

window = Tk()

window.resizable(height = None, width = None)
window.title("Hello Purr!")

loader = Image.open("Originals/purr.png")
image = ImageTk.PhotoImage(loader)
width = image.width()
height = image.height()

canvas = Canvas(window, width = int(width), height = int(height))
canvas.pack()
img = ImageTk.PhotoImage(loader)
canvas.create_image(0, 0, anchor=NW, image=img)

text = Label(window,text="Acaricia el Gat!", font=("Verdana",18))
text.pack()

#Lògica de control

def click(event):
    playsound('Originals/so.mp3')

       
canvas.bind("<Button-1>", click)


window.mainloop()
