import random

teploty = []
pocet_dni = 30

# naplní list náhodnými telotami od 10 do 30
for i in range(pocet_dni):
   # teploty[] = random.randint(10,30) # vráti chybu, lebo prvky ešte neexistujú
    teploty.append(random.randint(10,30))


for i in range(pocet_dni):
    print(f"{i+1}. deň - {teploty[i]}°C")

# vypočíta a vypíše priemernú teplotu
# piemerna_teplota = sum(teploty) / pocet_dni
# print(piemerna_teplota)
suma = 0
for i in range(pocet_dni):
    suma += teploty[i]
piemerna_teplota = suma / pocet_dni
print(f"Priemerná teplota v mesiaci je {piemerna_teplota}°C")


print("Dni s podpriemernou teplotou: ")
deň = 0
for teplota in teploty:
    deň +=1
    if teplota < piemerna_teplota:
        print(f"{deň}. deň - {teplota}°C")

# D.Ú. urob max(teplota) a min(teplota) bez funkcií

max = 0
for teplota in teploty:
    if teplota > max:
        max = teplota
print (f"Najviššia teplota bola {max}°C")


min = 30
for teplota in teploty:
    if teplota < min:
        min = teplota
print (f"najnižšia teplota bola {min}°C")