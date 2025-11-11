# zadania_list_comp.py
# 9 zadań z list comprehensions — od prostych po trudne

# ------------------------
# 🟢 ŁATWE
# ------------------------

# 1️⃣ Podwojenie liczb
liczby = [1, 2, 3, 4, 5]
wynik = [i * 2 for i in liczby]
print("1) Podwojenie liczb:", wynik)  # [2, 4, 6, 8, 10]

# 2️⃣ Liczby parzyste
liczby = [3, 6, 7, 8, 9, 12]
parzyste = [i for i in liczby if i % 2 == 0]
print("2) Liczby parzyste:", parzyste)  # [6, 8, 12]

# 3️⃣ Długości słów
slowa = ["kot", "pies", "papuga"]
dlugosci = [len(s) for s in slowa]
print("3) Długości słów:", dlugosci)  # [3, 4, 6]

# ------------------------
# 🟡 ŚREDNIE
# ------------------------

# 4️⃣ Kwadraty liczb większych od 5
liczby = [2, 4, 6, 8, 10]
kwadraty = [i**2 for i in liczby if i > 5]
print("4) Kwadraty liczb > 5:", kwadraty)  # [36, 64, 100]

# 5️⃣ Słowa zaczynające się na "a"
slowa = ["ala", "kot", "adam", "pies", "ananas"]
na_a = [s for s in slowa if s.startswith("a")]
print('5) Słowa zaczynające się na "a":', na_a)  # ['ala', 'adam', 'ananas']

# 6️⃣ Liczby 1–10 jako stringi
strings = [str(i) for i in range(1, 11)]
print("6) Liczby jako stringi:", strings)
# ["1", "2", "3", ..., "10"]

# ------------------------
# 🔴 TRUDNE
# ------------------------

# 7️⃣ Macierz kwadratów (3x3)
macierz = [[i**2 for i in range(1, 4)] for _ in range(3)]
print("7) Macierz kwadratów:", macierz)
# [[1, 4, 9], [1, 4, 9], [1, 4, 9]]

# 8️⃣ Dodatnie liczby do kwadratu
liczby = [-4, -2, 0, 1, 3, 5]
wynik = [i**2 for i in liczby if i > 0]
print("8) Kwadraty liczb dodatnich:", wynik)  # [1, 9, 25]

# 9️⃣ Odwrócone słowa dłuższe niż 3 litery
slowa = ["kot", "pies", "mysz", "lew", "tygrys"]
odwrocone = [s[::-1] for s in slowa if len(s) > 3]
print("9) Odwrócone słowa >3 litery:", odwrocone)
# ["seip", "zsym", "syrgyt"]
