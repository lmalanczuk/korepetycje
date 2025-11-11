# list_comprehensions_wyjasnienie.py
# -----------------------------------
# Wprowadzenie do "list comprehensions" w Pythonie
# (czyli: jak zrobić listę w jednej linijce zamiast długiej pętli)

# 🔹 1. Zaczynamy od czegoś, co każdy zna — zwykła pętla i .append()

liczby = [1, 2, 3, 4]

# Chcemy stworzyć nową listę, w której każda liczba będzie *2
nowe = []
for i in liczby:
    nowe.append(i * 2)

print("Zwykła pętla:", nowe)  # [2, 4, 6, 8]


# 🔹 2. To samo można zapisać krócej, w jednej linijce:
# Składnia list comprehension wygląda tak:
# [co_ma_byc_wpisane for zmienna in lista]

nowe2 = [i * 2 for i in liczby]
print("List comprehension:", nowe2)  # [2, 4, 6, 8]

# 💡 Czytamy to po polsku:
# "Zrób i*2 dla każdego i z listy liczby"


# 🔹 3. Możemy też dodać warunek (filtr) na końcu:
# [co_ma_byc_wpisane for zmienna in lista if warunek]

liczby = [3, 6, 7, 8, 9, 12]
parzyste = [i for i in liczby if i % 2 == 0]
print("Tylko liczby parzyste:", parzyste)  # [6, 8, 12]

# 💬 Czytaj to jak zdanie:
# "Weź i dla każdego i z listy liczby, jeśli i jest parzyste."


# 🔹 4. List comprehension to NIE jest nowa funkcja — to skrót
# Poniższe dwa fragmenty robią dokładnie to samo:

# wersja długa:
wynik1 = []
for i in liczby:
    if i % 2 == 0:
        wynik1.append(i**2)

# wersja krótka:
wynik2 = [i**2 for i in liczby if i % 2 == 0]

print("Długa wersja:", wynik1)
print("Krótka wersja:", wynik2)


# 🔹 5. Można stosować różne operacje:
slowa = ["kot", "pies", "papuga"]
dlugosci = [len(s) for s in slowa]  # długości słów
duze = [s.upper() for s in slowa]   # duże litery
filtr = [s for s in slowa if len(s) > 3]  # tylko słowa >3 litery

print("Długości słów:", dlugosci)
print("Duże litery:", duze)
print("Słowa dłuższe niż 3:", filtr)


# 🔹 6. Można też robić listy z list (tzw. zagnieżdżone comprehensions)
macierz = [[i**2 for i in range(1, 4)] for _ in range(3)]
print("Macierz kwadratów:", macierz)
# [[1, 4, 9], [1, 4, 9], [1, 4, 9]]


# 🔹 7. Analogia – sokowirówka 🍎
# Wyobraź sobie, że masz sokowirówkę.
# Wkładasz owoce (lista wejściowa),
# filtrujesz tylko jabłka (if warunek),
# i zamieniasz na sok (operacja w nawiasie kwadratowym).

# Przykład:
owoce = ["jabłko", "banan", "gruszka", "jabłko"]
sok = [f"sok z {o}" for o in owoce if o == "jabłko"]
print("Sokowirówka:", sok)  # ['sok z jabłko', 'sok z jabłko']


# 🔹 8. Dla porównania — różne typy comprehension:

# set comprehension (zbiór)
zbior = {i for i in [1, 2, 2, 3, 3, 3]}
print("Set comprehension:", zbior)  # {1, 2, 3}

# dict comprehension (słownik)
slownik = {i: i**2 for i in range(1, 5)}
print("Dict comprehension:", slownik)  # {1: 1, 2: 4, 3: 9, 4: 16}

# generator (nie lista, tylko leniwa wersja)
generator = (i**2 for i in range(3))
print("Generator:", list(generator))  # [0, 1, 4]

# 🎯 Zapamiętaj:
# [co zrobić for zmienna in lista if warunek]
# To po prostu skrót od pętli + if + append.