import turtle

t = turtle.Turtle()
dlzka = 50

def stlpec(d):
    for i in range(4):
        t.forward(d)
        t.right(90)

stlpec(dlzka)
t.penup()
t.forward(dlzka)
t.right(90)
t.pendown()
t.penup()
t.forward(dlzka)
t.pendown()
stlpec(dlzka)
t.penup()
t.forward(dlzka)
t.pendown()
stlpec(dlzka)
t.penup()
t.forward(dlzka)
t.pendown()
stlpec(dlzka)
t.penup()
t.forward(dlzka)
t.pendown()
stlpec(dlzka)
t.penup()
t.forward(dlzka)
t.pendown()
stlpec(dlzka)
t.penup()
t.forward(dlzka)
t.pendown()
stlpec(dlzka)




turtle.mainloop()