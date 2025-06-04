import datetime

class Osoba: # triedy, vždy píšeme prvým veľkým písmenom
    def __init__(self, meno, priezvisko, rok): # konštruktor, zavolá sa pri vzniku objektu
        self.meno = meno # atribút objektu (vlastnosť)
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self): # metóda (čo vie objekt robiť)
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek} rokov.")

    def vypis_meno(self):
        print(self.meno , self.priezvisko)

    def vypis_vek(self):
        print(self.vek)

    def vypis_rok(self):
        print(self.rok)


class Student(Osoba): # trieda Student zdedí astribúty a metódy od triedy Osoba
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok) # super - znamená, že použije atribúty z rodičovskej triedy (Osoba)
        # Osoba.__init__(meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        super().pozdrav()
        print(f"Som študentom {self.trieda} triedy.")
        # polymorfizmus - meníme metódu pozdrav z rodičovskej triedy (Osoba)

    
# miso = Osoba("Michal", "Šutek", 1978) # vznikne objekt miso, vytvorený pomocou triedy Osoba
# miso.pozdrav() # voláme metódu objekt pozdrav
# fero = Osoba("František","Mikuláško", 1990)
# fero.pozdrav()

# miso.vypis_meno()
# miso.vypis_rok()
# miso.vypis_vek()

student = Student("Ján", "Študent", 2008, "I.AT")
student.pozdrav()
student.vypis_meno()
student.vypis_rok()
student.vypis_vek()

clovek = Osoba("Jurko", "Mrkvička", 2000)
clovek.pozdrav()