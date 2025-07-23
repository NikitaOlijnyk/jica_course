wyniki = (45, 67, 82, 90, 55, 74, 100, 61)


average = sum(wyniki) / len(wyniki)
print(f"srednia:{average}")
a = 0
for i in range(len(wyniki)):
    if wyniki[i] > average:
        print(f"{wyniki[i]} zdobyl uczestnik nr {i+1}")
    if wyniki[i] >= 60:
        a +=1
    if i == 100:
        print(f"Gratulacje dla najlepszego uczestnika! {i+1}")
print(f"{a} uczestnikow zdalo")

