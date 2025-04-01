ret = "Ahoj svet"
ret1 = ret[:6]
ret2 = ret[5:1]
print(ret1)
print(ret2)
# ret[5] = "s" # toto nie je dovolené v Pythone
novyret = ret[:5] + "s" + ret[6:]
print(novyret)
novyret = novyret + " svet "
print(novyret)
novyret = 3* (novyret + " ")
print(novyret)