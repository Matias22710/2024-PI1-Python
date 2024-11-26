import tkinter , random

pocet = int(input("Zadaj počet jednotiek:\n"))

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

for i in range(pocet):
    x = random.randint(3, 1000-30-3)
    y = random.randint(3, 1000-70-3)
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y, x+20, y+10, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+10, x+20, y+20, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+30, x+20, y+40, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+40, x+20, y+50, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+50, x+20, y+60, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+60, x+20, y+70, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x, y+60, x+10, y+70, fill=random.choices(["red", "blue", "green"]))
    canvas.create_rectangle(x+10, y+60, x+20, y+70, fill=random.choices(["red", "blue", "green"]))


canvas.mainloop()