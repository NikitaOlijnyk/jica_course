uczen = {
    "imie": "Wiktor",
    "nazwisko": "nie znaju",
    "rok": 20,
    "kierunek": "IT",
    "oceny": [6, 6, 5, 3, 4, 7]
}

print(sum(list(uczen.values())[4]) / len(list(uczen.values())[4]))
print(sum(uczen['oceny']) / len(uczen['oceny']) )