import tkinter , random
canvas = tkinter.Canvas

canvas_width = int(input("Šírka plátna: "))
canvas_height = int(input("Výška plátna: "))

canvas = tkinter.Canvas(height=canvas_height , width=canvas_width)
canvas.pack()

for i in range(100):
    a = random.randint(1, 30)
    x = random.randint(3, canvas_width-3-a)
    y = random.randint(3, canvas_height-3-a)
    if a < 10:
        farba = "red"
    elif a < 20:
        farba = "green"
    else:
        farba = "blue"
    canvas.create_rectangle(x, y, x + a, y + a, fill=farba, width=0)

tkinter.mainloop()