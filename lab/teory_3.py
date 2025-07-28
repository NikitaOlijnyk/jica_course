a =int(input("wpisz liczbe:"))

if a%60 > 0:
    print(f"{a//60} godzin {a%60} minut")
else:
    print(f"{a//60} godzin")