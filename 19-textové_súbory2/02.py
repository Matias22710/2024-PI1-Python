import tkinter as tk
import random

def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def draw_chess_pieces():
    window = tk.Tk()
    window.title("Šachové figúrky")

    canvas = tk.Canvas(window, width=800, height=200, bg="white")
    canvas.pack()

    chess_pieces = ['\u2654', '\u2655', '\u2656', '\u2657', '\u2658', '\u2659']

    x_pos = 50

    for piece in chess_pieces:
        color = random_color()  
        canvas.create_text(x_pos, 100, text=piece, font=('Arial', 50), fill=color)
        x_pos += 100 

    window.mainloop()