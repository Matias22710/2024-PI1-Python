import tkinter as tk
import random

root = tk.Tk()
root.title("Pexeso")

grid_size = 4

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:(grid_size ** 2 // 2)]

cards = letters + letters
random.shuffle(cards)

exposed = []
matches = 0
turns = 0

def on_card_click(i, j):
    global exposed, matches, turns

    card_index = i * grid_size + j

    if card_index not in exposed:
        exposed.append(card_index)
        buttons[i][j].config(text=cards[card_index], state="disabled", fg="black")

        if len(exposed) == 2:
            turns += 1
            root.after(500, check_match)


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

buttons = []
for i in range(grid_size):
    row_buttons = []
    for j in range(grid_size):
        button = tk.Button(root, text=" ", width=10, height=3,
                           command=lambda i=i, j=j: on_card_click(i, j), fg="black")
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()