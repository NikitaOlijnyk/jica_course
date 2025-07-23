from itertools import product

produkty = ("mleko", "chleb", "masło", "ser", "jabłka", "piwo", "salo", "kwas", "miamore", "pomidor")

koszyk = list(input("Wpisz 3 produkrty do swojego koszyka: ").split())

tuple_koszyk = tuple(koszyk)


for i in tuple_koszyk:
    a = 0
    for j in produkty:
        if i != j:
            a +=1
        if i == j:
            print(f"Produkt {i} jest dostepny")
    if a == 10:
        print(f"Produkt {i} nie dostepny")


print(sorted(koszyk))


