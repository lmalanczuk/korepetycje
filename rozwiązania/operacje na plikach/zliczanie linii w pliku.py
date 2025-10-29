# otwieramy plik w trybie tylko do odczytu
with open("tekst.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # wczytanie wszystkich linii do listy

# len() zwraca długość listy, czyli liczbę linii
print("Liczba wierszy w pliku:", len(lines))