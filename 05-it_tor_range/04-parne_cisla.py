cislo = int(input("Zadaj čislo: "))

# vypis parnych cisiel
print(f"Párne čísla do {cislo}:")
for i in range(2, cislo+1, 2):
    print(i)

# vypis neparnych cisiel
print(f"Nepárne čísla do {cislo}:")
for i in range(1, cislo+1, 2):
    print(i)

cislo = int(input("Zadaj číslo"))
if cislo%2 == 0:
    print("párne")
else:
    print("nepárne")

if cislo % 2 == 0:
    print(f"Číslo {cislo} je párne.")
else:
    print(f"číslo {cislo} je nepárne.")