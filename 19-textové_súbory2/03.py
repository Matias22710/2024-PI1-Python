import tkinter as tk
import random
def nakresli_sachove_figurky():
    figurky = ''.join(chr(0x2654 + i) for i in range(6))
    okno = tk.Tk()
    platno = tk.Canvas(okno, width=600, height=100, bg='white')
    platno.pack()
    for i, figura in enumerate(figurky):
        farba = "#" + ''.join(random.choices('0123456789ABCDEF', k=6))
        platno.create_text(50 + i*90, 50, text=figura, font=('Arial', 50), fill=farba)

    okno.mainloop()
    
nakresli_sachove_figurky()