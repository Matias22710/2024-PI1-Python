def kresli(retazec):
    # Počiatočné nastavenie
    pero_dole = False  # Začneme s perom hore
    x, y = 0, 0  # Počiatočná pozícia

    # Pre každý znak v retazci robíme príslušnú akciu
    i = 0
    while i < len(retazec):
        prikaz = retazec[i]

        if prikaz == 's':
            # Pohyb doľava
            if pero_dole:
                print(f"Kreslíme doľava z ({x}, {y})")
            x -= 1
        elif prikaz == 'v':
            # Pohyb nahor
            if pero_dole:
                print(f"Kreslíme nahor z ({x}, {y})")
            y += 1
        elif prikaz == 'j':
            # Pohyb doprava
            if pero_dole:
                print(f"Kreslíme doprava z ({x}, {y})")
            x += 1
        elif prikaz == 'z':
            # Pohyb nadol
            if pero_dole:
                print(f"Kreslíme nadol z ({x}, {y})")
            y -= 1
        elif prikaz == 'h':
            # Pero hore (nepohybujeme sa, len zrušíme kreslenie)
            pero_dole = False
            print(f"Pero hore na pozícii ({x}, {y})")
        elif prikaz == 'd':
            # Pero dole (začneme kresliť)
            pero_dole = True
            print(f"Pero dole na pozícii ({x}, {y})")
        elif prikaz.isdigit():
            # Ak je znak číslica, opakujeme nasledujúci príkaz
            pocet_opakovani = int(prikaz)
            i += 1  # Preskakujeme číslicu a pokračujeme so znakmi
            sub_retazec = retazec[i:i+pocet_opakovani]
            print(f"Opakujeme: {sub_retazec} {pocet_opakovani} krát")
            kresli(sub_retazec * pocet_opakovani)  # Rekurzívne volanie s opakovaním
            i += len(sub_retazec) - 1  # Pokračujeme za opakovaný príkaz

        i += 1

kresli('4v4j4z4sh5vd' * 5)