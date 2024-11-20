import tkinter
import random as tk

pocet = int(input("Zadaj počet jednotiek: "))

canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()

def jednotka(x, y):
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=random.choice(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y, x+20, y+10, fill=random.choice(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+10, x+20, y+20, fill=random.choice(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill=random.choice(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+30, x+20, y+40, fill=random.choice(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+40, x+20, y+50, fill=random.choice(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+50, x+20, y+60, fill=random.choice(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+60, x+20, y+70, fill=random.choice(["red", "blue", "green"]))




canvas.mainloop()