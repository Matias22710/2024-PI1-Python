def pocet(retazec, podretazec):
    pocet_vyskytov = 0
    i = 0
    
    # Pokračujeme, kým nezostane dosť znakov na to, aby sme mohli hľadať podreťazec
    while i <= len(retazec) - len(podretazec):
        # Ak sa podreťazec začína na pozícii i
        if retazec[i:i+len(podretazec)] == podretazec:
            pocet_vyskytov += 1
            # Posunieme sa za nájdený podreťazec, aby sme nezapočítali rovnaký výskyt viackrát
            i += len(podretazec)
        else:
            # Ak podreťazec nevyhovuje, pokračujeme na ďalšiu pozíciu
            i += 1
    
    return pocet_vyskytov

# Testovacie prípady
print(pocet('mama ma emu a ema ma mamu', 'ma '))  # Výstup: 4
print(pocet('mama ma emu a ema ma mamu', 'am'))   # Výstup: 2