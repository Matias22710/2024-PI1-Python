teploty=[10, 13, 15, 20]
print(teploty)
print(teploty[0])

nakup = ["chlieb","maslo","mlieko"]
print(nakup)
print(nakup[1])

zviera= ["pes","Dunčo",2020,"hnedá",10.7]  # do listu môžeme ukladať hodnoty rôznych typov (int, str, bool)
print(zviera)
print(zviera[2])

# v Pythone sú listy dinamické, to znamená, že nemusia mať definovanú veľkosť (počet prvkov)
# prvky pridávame pomocou funkcie append()
prázdny = []
print(prázdny)
prázdny.append("Ahoj")
print(prázdny)
prázdny.append("120")
prázdny.append(49)
print(prázdny[-1])

#  listy vieme aj zreťaziť (spočítať)
nakupyazvierata = nakup + zviera
print(nakupyazvierata)
print(3*zviera)

print("Dunčo" in zviera)

# na rozdiel od string sú listy v pythone mutable (meniteľné)
prázdny[0] = 1000
print(prázdny)

hodnoty = [15, 30, 80, 50, 100]
print(len(hodnoty))
print(sum(hodnoty))
print(min(hodnoty))
print(max(hodnoty))