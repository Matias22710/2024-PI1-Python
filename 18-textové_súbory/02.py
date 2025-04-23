# "subor.txt" je relatívna cesta k súboru (musí byť v tom istom priečinku ako samotný kód)
#otvorí súbor subor.txt na čítanie, pre zápis sa používa "w", "r" - read, "w" - write . Ak súbor neexistuje vypíše chybu.
# subor = open("c:/dokumenty/subor.txt", "r") - toto je absolútna cesta c:/dokumenty/subor.txt
# subor = open("../subor.txt", "r") .. je o priečinok vyššie
# subor = open("../16-list/subor.txt", "r") .. je o priečinok vyššie

# for i in range(4):
#     riadok = subor.readline() # readline prečíta celý riadok (od miesta kde sa aktuálne nachádza)
#     print(riadok)

# riadok = subor.readline()
# while riadok != "":
#     print(riadok)
#     riadok = subor.readline()