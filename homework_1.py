def licz_litery(tekst:str) -> dict:
    tekst = tekst.lower()
    result = {}
    for i in tekst:
        if i.isalpha():
            result[i] = tekst.count(i)
            print(i, tekst.count(i))
    print(result)

licz_litery("aA")