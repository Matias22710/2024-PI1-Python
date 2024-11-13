import tkinter

canvas = tkinter.Canvas(width = 600, height = 600)
canvas.pack()

def xko(x, y):
    canvas.create_rectangle(x, y, x+10, y+10, fill="red")
    canvas.create_rectangle(x, y+10, x+10, y+20, fill="red")
    canvas.create_rectangle(x+10, y+20, x+20, x+30, fill="red")
    canvas.create_rectangle(x+20, y+30, x+30, y+40, fill="red")
    canvas.create_rectangle(x+20, y+40, x+30, y+50, fill="red")
    canvas.create_rectangle(x+20, y+50, x+30, y+60, fill="red")
    canvas.create_rectangle(x+20, y+60, x+30, y+70, fill="red")

    
xko(10,10)

canvas.mainloop()