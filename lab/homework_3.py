km = float(input("ile km"))
l_km = float(input("ile litrow na 100km"))
cena_l = float(input("ile kosztuje litr"))
your_buddies = int(input("ile pasazerow masz"))


def summary_on_your_trip(km, l_km, cena_l, your_buddies):
    l = km/100*l_km
    print(f"{l:g} zuzyjesz na {km:g}km")
    print(f"cena tego{l*cena_l:g}")
    if your_buddies > 0:
        print(f"koszt na kazda osobe{l*cena_l/your_buddies:g}")
        if km > 500:
            print("Długa trasa – zaplanuj przerwy na odpoczynek!")

summary_on_your_trip(km, l_km, cena_l, your_buddies)