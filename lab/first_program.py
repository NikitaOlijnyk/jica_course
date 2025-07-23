bilet_normalny = 45
bilet_ulgowy = 35

age = int(input("Jaki masz wiek?"))
if age < 3 or age > 70:
    print("Masz za darmo, ziomiusz")
elif age < 26:
     print(f"Masz taka cene {bilet_ulgowy}, ziomiusz")
elif age > 26:
    print(f"Masz taka cene {bilet_normalny}, ziomiusz")
