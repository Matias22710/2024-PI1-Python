import tkinter as tk
import random

def akciaTlacidla():
    global pokusov
    pokusov += 1
    cisloMOJE = int(  textbox.get() )
    if cisloMOJE < cisloPC:
       label.config("Dal si menšie číslo")
    elif cisloMOJE < cisloPC:
         label.config("Dal si väčšie číslo")
    else:
         label.config(text = "Uhádol si")

root = tk.Tk()
root.geometry("200,200")

cisloPC = random.randint(0,9)
pokusov = 0

label = tk.Label(root, tex = cisloPC)
label.pack()

textbox = tk.Entry(root)
textbox.pack()

button = tk.Button(root, text = "Hádaj", command=akciaTlacidla)
button.pack()

root.mainloop()