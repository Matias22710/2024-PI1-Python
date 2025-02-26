# string je reťazec znakov napr. "Ahoj"
# reťazec začíname a končíme "" alebo ''
# \n - nový riadok, \t - tabulátor, \" - "
# funkcia len() - vráti dĺžku reťazca (počet znakov)
# znaky v reťazci sú indexované - prvý znak má index 0
# index píseme do hranatých zátvoriek [] - p.alt+f, p.alt+g

retazec = "Ahoj Svet"
print(retazec)
print(len(retazec))
# print(retazec[0])
# print(retazec[1])

# for i in range(len(retazec)):
#     print(retazec[i])

for znak in retazec: # postupne vyberá znaky z reťazca do premennej znak
    print(znak)