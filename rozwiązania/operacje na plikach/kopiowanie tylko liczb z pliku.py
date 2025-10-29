with open("dane.txt", "r", encoding="utf-8") as dane, \
        open("liczby.txt", "w", encoding="utf-8") as liczby:
    for line in dane:
        line = line.strip()  # usuwa białe znaki (np. \n)
        if line.isdigit():  # sprawdza, czy linia zawiera tylko cyfry
            liczby.write(line + "\n")

print("Liczby zostały zapisane w pliku liczby.txt.")