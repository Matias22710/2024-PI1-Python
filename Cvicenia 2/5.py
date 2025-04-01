import tkinter as tk

def stvorce(retazec, vel=60):
    # Rozdelíme vstupný reťazec na jednotlivé časti
    prvky = retazec.split()
    
    # Pre každú farbu kontrolujeme, či predchádza číslo (veľkosť)
    farby_a_velkosti = []
    i = 0
    while i < len(prvky):
        if prvky[i].isdigit():  # Ak je prvok číslo, znamená to veľkosť
            velkost = int(prvky[i])
            farba = prvky[i + 1]  # Farba je nasledujúci prvok
            farby_a_velkosti.append((farba, velkost))
            i += 2
        else:
            # Ak číslo nie je prítomné, použijeme predvolenú veľkosť
            farby_a_velkosti.append((prvky[i], vel))
            i += 1

    # Nastavenie šírky plochy
    sirka = 450
    canvas = tk.Canvas(width=sirka, height=200)
    canvas.pack()

    # Inicializujeme pozíciu pre kreslenie štvorcov
    x = 10  # Počiatočná pozícia na osi x

    # Rozmiestnenie štvorcov na plochu
    while x < sirka:
        for farba, velkost in farby_a_velkosti:
            if x + velkost > sirka:  # Ak by ďalší štvorce presiahli šírku, zastavíme
                break
            canvas.create_rectangle(x, 50, x + velkost, 50 + velkost, fill=farba)
            x += velkost  # Posúvame sa na ďalšiu pozíciu

    # Spustenie hlavného cyklu pre zobrazenie grafiky
    tk.mainloop()

# Príklad volania funkcie
stvorce('40 red 20 blue purple 40 red 30 gold')