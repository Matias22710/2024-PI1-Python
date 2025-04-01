# užívateľ zadá celú vetu a program vetu rozdelí na slová, ktoré vypíše náhodnou farbou na náhodnom mieste
# aj písmenká zo slov vypíše náhodnými farbami

import random , tkinter

veta = input("\n\nZadaj vetu:\n")
veta += " "

def rozdelenie(veta):
    slova = []
    skladanie = ""
    for i in veta:
        if ord(i) != 32:
            skladanie += i 
        else:
            slova += [skladanie]
            skladanie = ""
    for slovo in slova:
        vypis(slovo)       

def vypis(slovo):
    x = random.randint(50,600)
    y = random.randint(50,650)
    for pismeno in slovo:
        farba = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"
        canvas.create_text(x, y, text=pismeno, fill=farba, font="Arial 16")
        x += 14

canvas=tkinter.Canvas(width=700,height=700)
canvas.pack()

rozdelenie(veta)

canvas.mainloop()