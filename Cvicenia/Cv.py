import tkinter
import random

def vypis():
    text = 'Ahoj'
    x = random.randrange(60, 340)
    y = random.randrange(30, 250)
    canvas.create_text(x, y, text=text, font='arial 20')

canvas = tkinter.Canvas()
canvas.pack()
tlacidlo = tkinter.Button(text='Vypíš text', command=vypis)
tlacidlo.pack()

tkinter.mainloop()