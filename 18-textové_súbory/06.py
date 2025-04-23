import tkinter

canvas = tkinter.Canvas()
canvas.pack()

fbody = open('body.txt', "r")
for body in fbody:
    print(body)
    medzera = body.find(" ")
    x = body[:medzera]
    y = body[medzera:]
    print(x)
    print(y)
    canvas.create_oval(x-5, y-5, x+5, y+5)

tkinter.mainloop()