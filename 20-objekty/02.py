class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print(f'čas je {self.hodiny}:{self.minuty:02}')

    def str(self):
        return f'{self.hodiny}:{self.minuty:02}'

    def pridaj(self, hodiny, minuty):
        self.hodiny += hodiny
        self.minuty += minuty
        self.hodiny += self.minuty // 60
        self.minuty = self.minuty % 60

def neskor(cas, hodiny, minuty):
    novy = Cas(cas.hodiny, cas.minuty)
    novy.pridaj(hodiny, minuty)
    return novy

if __name__ == '__main__':

    c = Cas(9, 17)
    c.vypis()
    d = Cas(10, 5)
    d.vypis()

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
        dalsi = neskor(zoznam[-1], 0, 50)
        zoznam.append(dalsi)

    for c in zoznam:
        print(c.str(), end=' ')
    print()