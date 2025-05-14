class TelefonnyZoznam:
    def __init__(self, meno_suboru=None):
        self.zoznam = []
        self.meno_suboru = meno_suboru
        if meno_suboru:
            self.citaj()

    def pridaj(self, meno, telefon):
        for i, (m, t) in enumerate(self.zoznam):
            if m == meno:
                self.zoznam[i] = (meno, telefon)
                return
        self.zoznam.append((meno, telefon))

    def vypis(self):
        for meno, telefon in self.zoznam:
            print(f'{meno}: {telefon}')

    def zapis(self):
        if self.meno_suboru:
            with open(self.meno_suboru, 'w') as subor:
                for meno, telefon in self.zoznam:
                    subor.write(f'{meno};{telefon}\n')

    def citaj(self):
        if self.meno_suboru:
            self.zoznam = []
            try:
                with open(self.meno_suboru, 'r') as subor:
                    for riadok in subor:
                        meno, telefon = riadok.strip().split(';')
                        self.zoznam.append((meno, telefon))
            except FileNotFoundError:
                print(f'Chyba: Súbor {self.meno_suboru} neexistuje.')

tz = TelefonnyZoznam('tel.txt')
tz.pridaj('Jana', '0901020304')
tz.pridaj('Juro', '0911111111')
tz.pridaj('Jozo', '0212345678')
tz.pridaj('Jana', '0999020304')
tz.vypis()  
tz.zapis() 
t2 = TelefonnyZoznam('tel.txt') 
t2.vypis() 