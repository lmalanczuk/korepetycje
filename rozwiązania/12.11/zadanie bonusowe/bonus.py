def main():
    dane = []
    with open("temperatury.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data, temp, opady = line.split(";")
            dane.append((data, float(temp), float(opady)))

    # 1) dni > 25°C
    dni_cieple = [d for d in dane if d[1] > 25]
    liczba_cieplych = len(dni_cieple)

    # 2) najcieplejszy dzień
    najcieplejszy = max(dane, key=lambda x: x[1])

    # 3) średnia temperatura przy opadach
    dni_z_opadami = [d[1] for d in dane if d[2] > 0]
    if dni_z_opadami:
        srednia_opady = round(sum(dni_z_opadami) / len(dni_z_opadami), 2)
    else:
        srednia_opady = 0

    # 4) najdłuższy ciąg dni bez opadów
    najlepszy_start = None
    najlepszy_koniec = None
    najlepsza_dlugosc = 0

    obecny_start = None
    obecna_dlugosc = 0

    for i, (data, temp, opady) in enumerate(dane):
        if opady == 0:
            if obecna_dlugosc == 0:
                obecny_start = data
            obecna_dlugosc += 1
            if obecna_dlugosc > najlepsza_dlugosc:
                najlepsza_dlugosc = obecna_dlugosc
                najlepszy_start = obecny_start
                najlepszy_koniec = data
        else:
            obecna_dlugosc = 0

    # 5) zapis suchych dni
    with open("suche_dni.txt", "w", encoding="utf-8") as out:
        for data, temp, opady in dane:
            if opady == 0:
                out.write(f"{data};{temp};{opady}\n")

    # wyniki
    with open("wyniki.txt", "w", encoding="utf-8") as out:
        out.write(f"1) Dni z temperaturą >25°C: {liczba_cieplych}\n")
        out.write(f"2) Najcieplejszy dzień: {najcieplejszy[0]} ({najcieplejszy[1]}°C)\n")
        out.write(f"3) Średnia temperatura przy opadach: {srednia_opady}°C\n")
        out.write(f"4) Najdłuższy okres bez opadów: {najlepsza_dlugosc} dni, "
                  f"od {najlepszy_start} do {najlepszy_koniec}\n")


if __name__ == "__main__":
    main()
