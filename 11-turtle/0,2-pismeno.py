import turtle

t = turtle.Turtle()# premennej t sa priradí korytnačka
dlzka = 50

def stvorec(d):
    for i in range(4):
        t.forward(d)
        t.left(90)

stvorec(dlzka)
t.penup()
t.forward(dlzka)
t.pendown()
stvorec(dlzka)

turtle.mainloop()