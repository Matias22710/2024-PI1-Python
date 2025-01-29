import turtle

t = turtle.Turtle()

pocet = 3
dlzka = 30

def schody(pocet, dlzka):
    for i in range(pocet):
        t.forward(dlzka)
        t.right(90)
        t.forward(dlzka)
        t.left(90)

for i in range(3):
    schody(pocet,dlzka)
    t.left(90)
    t.penup()
    t.forward(pocet * dlzka)
    t.right(90)
    t.pendown()


turtle.mainloop()
