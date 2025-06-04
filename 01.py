class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print(f"čas je {self.hodiny}:{self.minuty:02d}")

    def str(self):
        return f"{self.hodiny}:{self.minuty:02d}"

    def pridaj(self, hodiny, minuty):
        total_minuty = self.minuty + minuty
        total_hodiny = self.hodiny + hodiny + total_minuty // 60
        self.minuty = total_minuty % 60
        self.hodiny = total_hodiny % 24

def neskor(cas, hodiny, minuty):
    nova = Cas(cas.hodiny, cas.minuty)
    nova.pridaj(hodiny, minuty)
    return nova

if __name__ == '__main__':
    c = Cas(9, 17)
    c.vypis()
    d = Cas(10, 5)
    d.vypis()

    c = Cas(9, 1)
    print('teraz je', c.str())

    cas = Cas(17, 40)
    print('teraz je', cas.str())
    cas.pridaj(1, 35)
    print('neskôr', cas.str())

    c = Cas(17, 40)
    d = neskor(c, 2, 55)
    print(c.str())
    print(d.str())

    zoznam = [Cas(8, 10)]
    for i in range(14):
        zoznam.append(neskor(zoznam[-1], 0, 50))
    for c in zoznam:
        print(c.str(), end=' ')