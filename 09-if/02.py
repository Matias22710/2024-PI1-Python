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
   #if (x < canvas_width / 2) and (y < canvas_height / 2): # zložená podmienka, tzn. testujeme viac vlastností
        # medzi zložené podmienky vkladáme logické operátory (and = a zároveň, or = alebo)
   #     farba = "blue"
   #elif (x > canvas_width / 2) and (y > canvas_height / 2):
   #     farba = "yellow"
   # elif (x > canvas_width / 2) and (y < canvas_height / 2):
   #     farba = "red"
   # elif (x < canvas_width / 2) and (y > canvas_height / 2):
   #     farba = "green"
    
    if x < canvas_width / 2:
        if y < canvas...

    canvas.create_oval(x, y, x + a, y + a, fill=farba, width = 0)

tkinter.mainloop()