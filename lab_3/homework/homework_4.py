def odwroc_slowa(zdanie:str):
    zdanie = zdanie.split()
    result = []
    for i in zdanie:
        result.append(i[::-1])
    print(" ". join(result))



odwroc_slowa("ale ma kota")