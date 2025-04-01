import tkinter as tk
import random

# Zoznam Unicode znakov pre šachové figúrky
figury = ['\u2654', '\u2655', '\u2656', '\u2657', '\u2658', '\u2659']

# Funkcia na generovanie náhodnej farby
def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Vytvorenie hlavného okna
root = tk.Tk()
root.title("Šachové figúrky")

# Nastavenie veľkosti plochy
canvas = tk.Canvas(root, width=600, height=100)
canvas.pack()

# Pozícia pre vykreslenie figúrok
x = 10  # Počiatočná x-ová pozícia

# Nakreslíme všetky figúrky
for figura in figury:
    canvas.create_text(x, 50, text=figura, font=('Arial', 50), fill=random_color())
    x += 100  # Posunieme sa na ďalšie miesto pre ďalšiu figúrku

# Spustíme hlavný cyklus aplikácie
root.mainloop()