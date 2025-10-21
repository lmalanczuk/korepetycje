liczba = int(input("Podaj liczbę całkowitą: "))
silnia = 1
for i in range(1, liczba+1):
    silnia *=i

print(f"silnia: {silnia}")