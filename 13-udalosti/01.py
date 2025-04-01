import tkinter

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')

def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)
canvas.bind('<Motion>', tahaj)

tkinter.mainloop()