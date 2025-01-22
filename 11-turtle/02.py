import turtle
import random

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)

def posun():
    t.pu()
    t.setpos(random.randint(-100, 100), random.randint(-100, 100))
    t.seth(random.randint(0, 359))
    t.pd()

t = turtle.Turtle()
for i in range(10):
    posun()
    stvorec(30)
turtle.done()