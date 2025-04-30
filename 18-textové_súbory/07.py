import tkinter

x = []
y = []
tvary = []
farby = []

fbody = open("body.txt", "r")

def najdi_tvar():
    riadok = fbody.readline()
    if not riadok:
        return 
    riadok = riadok.strip()
    if riadok == "o":
        tvary.append("oval")
        najdi_farbu()
    elif riadok == "r":
        tvary.append("stvorec")
        najdi_farbu()
    else:
        najdi_tvar()  

def najdi_farbu():
    riadok = fbody.readline()
    if not riadok:
        return
    farba = riadok.strip()
    farby.append(farba)
    najdi_suradnice()

def najdi_suradnice():
    riadok = fbody.readline()
    if not riadok:
        return
    riadok = riadok.strip()
    medzera = riadok.find(" ")
    if medzera != -1:
        x.append(int(riadok[:medzera]))
        y.append(int(riadok[medzera+1:]))
        najdi_tvar()
    else:
        najdi_suradnice()

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

najdi_tvar()

for i in range(len(tvary)):
    if tvary[i] == "oval":
        canvas.create_oval(x[i]-10, y[i]-10, x[i]+10, y[i]+10, fill=farby[i])
    else:
        canvas.create_rectangle(x[i]-10, y[i]-10, x[i]+10, y[i]+10, fill=farby[i])

canvas.mainloop()