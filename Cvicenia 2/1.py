def sucet(retazec):
    # Rozdelíme reťazec podľa znaku '+' na jednotlivé čísla
    cisla = retazec.split('+')
    
    # Pre každý rozdelený reťazec prevedieme na celé číslo a sčítať ich
    return sum(int(cislo) for cislo in cisla)

# Testovanie funkcie
print(sucet('12+9'))  # 21
print(sucet('1+2+3+4'))  # 10
print(sucet('1234'))  # 1234