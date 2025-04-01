def ite_slovo(veta, ix):
    pozicia = 0  # Začneme na začiatku vety
    for i in range(ix):
        # Nájdeme pozíciu prvej medzery
        pozicia = veta.find(' ', pozicia)
        if pozicia == -1:  # Ak neexistuje ďalšia medzera, máme menej slov
            return ""  # Vrátime prázdny reťazec, ak ix je väčšie než počet slov
        pozicia += 1  # Posunieme sa za nájdenú medzeru
    
    # Teraz nájdeme ix-té slovo
    start = pozicia  # Začíname od pozície za predchádzajúcou medzerou
    pozicia = veta.find(' ', start)
    
    if pozicia == -1:
        # Ak žiadna ďalšia medzera neexistuje, znamená to, že sme na poslednom slove
        return veta[start:]
    else:
        # Ak nájdeme medzeru, slovo sa končí na tejto pozícii
        return veta[start:pozicia]
    
veta = "Toto je príklad vety"
print(ite_slovo(veta, 0))  # 'Toto'
print(ite_slovo(veta, 1))  # 'je'
print(ite_slovo(veta, 2))  # 'príklad'
print(ite_slovo(veta, 3))  # 'vety'
print(ite_slovo(veta, 4))  # ''