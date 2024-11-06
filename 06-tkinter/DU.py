import tkinter
canavas = tkinter.Canvas()
canavas.pack()

canavas.create_rectangle(10, 0, 0, 0, 50, fill="red")
canavas.create_rectangle(20, 20, 0, 40, 50, fill="red")
canavas.create_rectangle(30, 0, 30, 0, 50, fill="red")
canavas.create_rectangle(40, 0, 0, 0, 50, fill="red")
canavas.create_rectangle(50, 0, 0, 0, 50, fill="red")
tkinter.mainloop()