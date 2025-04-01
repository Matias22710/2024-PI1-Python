def ozatvorkuj(retazec, podretazec):
    # Použijeme metódu replace na náhradu podreťazca zátvorkami
    return retazec.replace(podretazec, f'({podretazec})')

# Príklady:
b = ozatvorkuj('Bratislava', 'a')
print(b)  # Výstup: 'Br(a)tisl(a)v(a)'

result = ozatvorkuj('prospešné programovanie v prologu', 'pro')
print(result)  # Výstup: '(pro)spešné (pro)gramovanie v (pro)logu'