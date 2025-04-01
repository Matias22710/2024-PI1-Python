def prevrat_poradie(veta):
    # Rozdelíme vetu na slová, pričom zohľadníme aj medzery a znaky konca riadku
    slova = veta.split()
    
    # Prevrátime poradie slov
    slova = slova[::-1]
    
    # Spojíme slová do reťazca s jednou medzerou medzi nimi
    return ' '.join(slova)

x = prevrat_poradie('Guido van Rossum')
print(x)  # Výstup: 'Rossum van Guido'

x2 = prevrat_poradie('Hello world\nHow are you?')
print(x2)  # Výstup: 'you? are How world Hello'