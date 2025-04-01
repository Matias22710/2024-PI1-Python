def usporiadaj(h1, h2, h3):
    # Najprv porovnáme hodnoty a zoradíme ich
    if h1 <= h2 and h1 <= h3:
        # h1 je najmenšie
        if h2 <= h3:
            return f"{h1} {h2} {h3}"
        else:
            return f"{h1} {h3} {h2}"
    elif h2 <= h1 and h2 <= h3:
        # h2 je najmenšie
        if h1 <= h3:
            return f"{h2} {h1} {h3}"
        else:
            return f"{h2} {h3} {h1}"
    else:
        # h3 je najmenšie
        if h1 <= h2:
            return f"{h3} {h1} {h2}"
        else:
            return f"{h3} {h2} {h1}"
        
x = usporiadaj('python', 'pytliak', 'pytagoras')
print(x)  # Výstup: 'pytagoras python pytliak'

x2 = usporiadaj(345, 123, 234)
print(x2)  # Výstup: '123 234 345'

x3 = usporiadaj('apple', 'banana', 'grape')
print(x3)  # Výstup: 'apple banana grape'