from tkinter import *
from random import *

w = 800
h = 800

def Figura():
    canvas.create_rectangle(0, 0, w, h, fill="white")

    x1 = randint(0, w)
    y1 = randint(0, h)
    x2 = randint(0, w)
    y2 = randint(0, h)
    x3 = randint(0, w)
    y3 = randint(0, h)

    color = "yellow"
    a =randint(1,4)
    if a == 1 :
        color = "red"
    elif a == 2 :
        color = "blue"
    elif a == 3 :
        color = "green"

    a =randint(1,3)
    if a == 1 :
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    elif a == 2 :
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)
    elif a == 3 :
        canvas.create_oval(x1, y1, x2, y2, fill=color)
        

root=Tk()

canvas=Canvas(root, width=w, height=h, bg='white')
canvas.pack()


button_1= Button(text='создать', command=Figura)
button_1.pack()

root.mainloop()
