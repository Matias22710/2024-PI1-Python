def posun_znak(znak, posun):
    # Skontrolujeme, či je znak malé písmeno
    if 'a' <= znak <= 'z':
        # Vypočítame nový znak v rámci abecedy s ohľadom na posun
        novy_znak = chr(((ord(znak) - ord('a') + posun) % 26) + ord('a'))
        return novy_znak
    # Ak to nie je malé písmeno, vrátime znak nezmenený
    return znak

def zakoduj(text, posun):
    # Použijeme posun_znak na každý znak v texte a vrátime nový zakódovaný text
    return ''.join(posun_znak(znak, posun) for znak in text)

# Príklady
x = zakoduj('pyThon', 10)
print(x)  # Výstup: 'ziTryx'

# Dekódovanie (posun o -10)
x_dekodovane = zakoduj(x, -10)
print(x_dekodovane)  # Výstup: 'pyThon'

# Skúšanie iného posunu (napr. 16)
x_posunute = zakoduj(x, 16)
print(x_posunute)  # Výstup: 'pyThon'