with open("tekst.txt", "r", encoding="utf-8") as f:
    content = f.read()  # wczytanie całej zawartości pliku
    words = content.split()  # podział po spacjach i nowych liniach

print("Liczba słów w pliku:", len(words))
