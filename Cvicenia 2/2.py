def vyhod_duplikaty(retazec):
    # Začíname s prázdnym reťazcom, do ktorého budeme pridávať znaky
    vysledok = ""
    
    # Prechádzame reťazcom a kontrolujeme každý znak
    for i in range(len(retazec)):
        # Ak je to prvý znak alebo sa aktuálny znak líši od predchádzajúceho
        if i == 0 or retazec[i] != retazec[i - 1]:
            vysledok += retazec[i]  # Pridáme znak do výsledného reťazca
    
    return vysledok

# Testovanie funkcie
x = vyhod_duplikaty('Braatisssllavaaaaa')
print(x)  # 'Bratislava'