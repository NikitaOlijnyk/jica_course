comment1 = list(input("Wpisz 1 komentarz: ").split())
comment2 = list(input("Wpisz 2 komentarz: ").split())
comment3 = list(input("Wpisz 3 komentarz: ").split())

all_comments = [*comment1, *comment2, *comment3]
unique_comments = set(x for x in all_comments if len(x) > 5)

print(len(unique_comments))


if "Python" or "python" in unique_comments:
    print("Uczestnicy lubią Pythona!")



