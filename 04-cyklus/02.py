n = int(input("Zadaj n: "))
sucet = 0
for i in range(n):
    sucet = sucet + (i+1)
# súčet + (i+1) je výraz? najskôr sa vypočíta výraz a výsledná hodnota sa priradí do premennej sucet
    #print(i, i+1, sucet)
print("súčet prvých", n ,"čísiel je ", sucet)