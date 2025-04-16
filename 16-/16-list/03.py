teploty = [12, 8, 15, 5, 19, 7]

maximum = teploty[0]
minimum = teploty[0]

for t in teploty:
    if t > maximum:
        maximum = t
    if t < minimum:
        minimum = t

# Výstup
print("Najvyššia teplota:", maximum)
print("Najnižšia teplota:", minimum)