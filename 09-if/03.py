import tkinter , random
canvas = tkinter.Canvas

canvas_width = int(input("Šírka plátna: "))
canvas_height = int(input("Výška plátna: "))

canvas = tkinter.Canvas(height=canvas_height , width=canvas_width)
canvas.pack()

for i in range(100):
    a = 10
    x = random.randint(canvas_width-3-a)
    y = random.randint(canvas_height-3-a)
    farba = "blue"
    

