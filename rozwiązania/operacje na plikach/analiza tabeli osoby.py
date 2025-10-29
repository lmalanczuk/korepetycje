with open("osoby.txt", "r", encoding="utf-8") as f, \
        open("pelnoletni.txt", "w", encoding="utf-8") as out:
    for line in f:
        line = line.strip()
        if not line:
            continue
        imie, nazwisko, wiek = line.split(";")
        if int(wiek) >= 18:
            out.write(f"{imie} {nazwisko}\n")

print("Dane pełnoletnich osób zapisano w pliku pelnoletni.txt.")
