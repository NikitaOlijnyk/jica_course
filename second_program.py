
cena_bileta = [30, 20, 15]

age = int(input("Jaki masz wiek?"))
is_student = input("Czy jestes studentem?")
day = input("Jaki dzien tygodnia?")
if day == "sroda":
    cena_bileta = [price - 5 for price in cena_bileta]
if age < 4:
    print("Masz za darmo, ziomiusz")
elif is_student == "tak" and age < 26:
    print(f"Masz taka cene {cena_bileta[1]}, ziomiusz")
elif age >= 65:
    print(f"Masz taka cene {cena_bileta[2]}, ziomiusz")
else:
    print(f"Masz taka cene {cena_bileta[0]}, ziomiusz")