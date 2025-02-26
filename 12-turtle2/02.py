import turtle
t = turtle.Turtle()

x = 0
y = 0 
x1 = 0

pocet1 = int(input("Zadaj počet domov a ulici:\n"))
pocet = int(input("Zadaj počet ulíc v dedine:\n"))
d = int(input("Zadaj veľkosť domov:\n"))
farba = input("Zadaj farbu domov:\n")
farba1 = input("Zadaj farbu striech:\n")
t.pensize(2)

def stvorec(d,farba):
    t.fillcolor(farba)
    for i in range(4):
     t.fd(d)
     t.rt(90)
     t.end_fill()

def okno(d):
    for i in range(4):
        stvorec(d/4,"blue")
        t.fd(d/2)
        t.rt(90)

def strecha(d,farba1):
    t.fillcolor(farba1)
    t.begin_fill()
    for i in range(3):
        t.fd(d)
        t.lt(120)
        t.end_fill()

def dom(d,farba,farba1):
    stvorec(d,farba)
    strecha(d,farba1)
    t.fd(d/4)
    t.rt(90)
    t.pu()
    t.fd(d/4)
    t.lt(90)
    t.pd()
    okno(d)

def ulica(d,farba,farba1,pocet,x,y):
    for i in range(pocet):
        t.setpos(x,y)
        t.pd()
        dom(d,farba,farba1)
        t.pu()
        x += d + 10

def dedina(d,farba,farba1,pocet,pocet1,x,y):
    for i in range(pocet1):
        ulica(d,farba,farba1,pocet,x,y)
        t.pu()
        x = x1
        y += d*2
        t.setpos(x,y)
        t.pd()

dedina(d,farba,farba1,pocet,pocet1,x,y) 

turtle.mainloop()