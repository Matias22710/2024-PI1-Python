n = int(input("zadaj n: "))
if n < 2:
    print(f" na {n}. políčku bude 1 zrnko ")
else:
    x = 2**(n - 1)
    print(f"na {n}. políčku bude {x} zrniek")