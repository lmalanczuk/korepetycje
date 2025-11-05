# 4_statystyki_liczb.py
def main():
    liczby = []
    with open("liczby.txt", "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                liczby.append(int(s))

    suma = sum(liczby)
    sr = suma / len(liczby) if liczby else 0
    maksimum = max(liczby) if liczby else None

    with open("wyniki.txt", "w", encoding="utf-8") as out:
        out.write(f"Suma: {suma}\n")
        out.write(f"Średnia: {sr}\n")
        out.write(f"Maksimum: {maksimum}\n")

if __name__ == "__main__":
    main()
