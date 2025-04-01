# range() - je funkcia, ktorá vygeneruje nejakú postupnosť
# range(5) - postupnosť 0,1,2,3,4
# range(od, po-1, krok)
# range môže mať aj klesajúcu postupnosť range(5, 0,-1)

print(list(range(5)))
print(list(range(2,5)))
print(list(range(2, 10, 2)))
print(list(range(5,0, -1)))

ret = "Ahoj"
for i in range(len(ret) -1, -1, -1):
    print(ret[i])