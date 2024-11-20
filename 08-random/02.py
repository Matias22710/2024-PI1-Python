import tkinter
import random

dlzka = int(input("Zadaj dĺžku štvorca: "))
pocet = int(input("Zadaj počet štvorcov: "))

canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()



for i in range(pocet):
   x = random.randint(3,500-dlzka-3)
   y = random.randint(3, 400-dlzka-3)
   canvas.create_rectangle(x, y, x+dlzka, y+dlzka, fill=random.choice(["red", "green", "blue", "yellow"]))


tkinter.mainloop()