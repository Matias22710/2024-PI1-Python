import tkinter as tk
import random

# Hlavné okno aplikácie
root = tk.Tk()
root.title("Pexeso")

# Počet kariet (4x4 matica)
grid_size = 4

# Zoznam písmen pre zadné strany kariet
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:(grid_size ** 2 // 2)]

# Karty, každý pár písmen sa zopakuje
cards = letters + letters
random.shuffle(cards)

# Premenné na sledovanie stavu hry
exposed = []  # Zoznam otočených kariet
matches = 0
turns = 0

# Funkcia na kliknutie na kartu
def on_card_click(i, j):
    global exposed, matches, turns

    card_index = i * grid_size + j

    if card_index not in exposed:
        exposed.append(card_index)
        buttons[i][j].config(text=cards[card_index], state="disabled", fg="black")

        if len(exposed) == 2:
            turns += 1
            root.after(500, check_match)

# Funkcia na overenie zhodnosti dvoch kariet
def check_match():
    global exposed, matches

    first_card_index = exposed[0]
    second_card_index = exposed[1]

    if cards[first_card_index] == cards[second_card_index]:
        matches += 1
        if matches == (grid_size ** 2) // 2:
            print(f"Gratulujeme! Vyhrali ste za {turns} ťahov.")
    else:
        first_i, first_j = divmod(first_card_index, grid_size)
        second_i, second_j = divmod(second_card_index, grid_size)
        
        buttons[first_i][first_j].config(text=" ", state="normal", fg="black")
        buttons[second_i][second_j].config(text=" ", state="normal", fg="black")

    exposed.clear()

# Vytvorenie tlačidiel pre karty
buttons = []
for i in range(grid_size):
    row_buttons = []
    for j in range(grid_size):
        button = tk.Button(root, text=" ", width=10, height=3,
                           command=lambda i=i, j=j: on_card_click(i, j), fg="black")
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Spustenie aplikácie
root.mainloop()