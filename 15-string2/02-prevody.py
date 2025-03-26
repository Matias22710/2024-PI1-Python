# print(bin(255)) # vypíše číslo v binárnej podobe
# print(hex(255)) # vypíše číslo v hexadecimálnej podobe
# print(0b11111111) # vypíše binárne číslo v desiatkovej podobe
# print(0xFF) # vypíše hexadecimálne číslo v desiatkovej podobe

def dec_bin(cislo):
    binarne = ""
    while cislo > 0:
        zvysok = cislo % 2
        binarne = str(zvysok) + binarne
        cislo = cislo // 2
    return binarne

def dec_hex(cislo):
    hexadecimalne = ""
    while cislo > 0:
         zvysok = cislo % 16
         if zvysok < 10:
             hexadecimalne =  str(zvysok) + hexadecimalne
        #  elif zvysok == 10:
        #       hexadecimalne = "A" + hexadecimalne
        #  elif zvysok == 11:
        #       hexadecimalne = "B" + hexadecimalne
        #  elif zvysok == 12:
        #       hexadecimalne = "C" + hexadecimalne
        #  elif zvysok == 13:
        #        hexadecimalne = "D" + hexadecimalne
        #  elif zvysok == 14:
        #        hexadecimalne = "E" + hexadecimalne
        #  elif zvysok == 15:
        #        hexadecimalne = "F" + hexadecimalne
        #  cislo = cislo // 16
         else:
            hexadecimalne = chr(55 + zvysok) + hexadecimalne
         cislo = cislo // 16
    return hexadecimalne

cislo = 255
print(dec_bin(cislo))
print(dec_hex(cislo))