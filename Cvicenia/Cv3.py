import tkinter as tk
root = tk.Tk()
root.geometry("200x200")

def akcia():
    label.config(text = textbox.get() )

label = tk.Label (root, text = "Som LABEL")
label.pack()

textbox = tk.Entry(root)
textbox.pack()

button = tk.Button(root, text = "Som TLAČIDLO", command=akcia)
button.pack()

root.mainloop()