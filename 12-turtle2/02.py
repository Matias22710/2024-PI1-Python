import turtle
t = turtle.Turtle()

pocet = 1
dlzka = 50 
dlzkas = 35
dlzkao = 20
dlzkaok = 10


def dom(d):
    t.fillcolor("red")
    t.begin_fill()
    for i in range(4):
        t.forward(dlzka)
        t.left(90)
    t.end_fill()

for i in range(1):
    dom(dlzka)
    t.forward(dlzka)
    t.left(90)
    t.penup()
    t.forward(dlzka)
    t.pendown()

    t.fillcolor("blue")
    t.begin_fill()
    for i in range(1):
        t.left(45)
        t.forward(dlzkas)
        t.left(90)
        t.forward(dlzkas)
    t.end_fill()

    dom(dlzkas)
    t.left(45)
    t.forward(dlzkas)
    t.left(90)
    t.forward(dlzkas)
    t.left(45)
    t.penup()
    t.forward(dlzka)
    t.left(135)
    t.forward(20)
    t.right(45)
    t.pendown()
    t.forward(dlzkao)
    t.left(90)
    t.forward(dlzkao)
    t.left(90)
    t.forward(dlzkao)
    t.left(90)
    t.forward(dlzkao)

    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.forward(dlzkaok)
        t.left(90)
        t.forward(dlzkaok)
        t.left(90)
        t.forward(dlzkaok)
        t.left(90)
        t.forward(dlzkaok)
        t.left(180)
        t.forward(20)
        t.right(180)
        t.forward(dlzkaok)
        t.right(90)
        t.forward(dlzkaok)
    t.end_fill()

    

turtle.mainloop()