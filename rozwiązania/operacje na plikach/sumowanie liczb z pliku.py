with open("liczby.txt", "r", encoding="utf-8") as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

if numbers:
    total = sum(numbers)
    avg = total / len(numbers)
    max_val = max(numbers)

    with open("wyniki.txt", "w", encoding="utf-8") as out:
        out.write(f"Suma: {total}\n")
        out.write(f"Średnia: {avg}\n")
        out.write(f"Największa wartość: {max_val}\n")

    print("Wyniki zapisane w pliku wyniki.txt.")
else:
    print("Plik liczby.txt jest pusty.")
