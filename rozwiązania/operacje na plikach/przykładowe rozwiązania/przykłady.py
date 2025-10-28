# 1) Wczytaj i wypisz bez pustych linii
# Cel: podstawy open, iteracja po liniach, end=''.
# Wskazówka: print(line, end='') nie dodaje dodatkowego \n.

# with open(r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line, end="")

#================================================================================================================
# 2) Wczytaj cały plik naraz i policz znaki
# Cel: read() i długość tekstu.

# with open(r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst.txt", "r", encoding="utf-8") as f:
#     data = f.read()
# print("\n", len(data))  # liczba znaków, łącznie z \n

#================================================================================================================
# 3) Policz liczbę wierszy, słów i znaków
# Cel: rozbicie na linie i słowa, metryki.

# with open(r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# line_count = len(lines)
# word_count = sum(len(l.split()) for l in lines)
# char_count = sum(len(l) for l in lines)
#
# print(line_count, word_count, char_count)
# Dla podanego pliku: 4, 12, (znaki zależne od dokładnych \n)

#================================================================================================================
# 4) Wypisz linie ponumerowane
# Cel: enumerate(start=1), strip().

# with open(r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst.txt", "r", encoding="utf-8") as f:
#     for i, line in enumerate(f, start=1):
#         print(f"{i}: {line.strip()}")

#================================================================================================================
# 5) Wyszukaj linie zawierające słowo (case-insensitive)
# Cel: filtrowanie, lower().

# needle = "kot"
# with open(r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst.txt", "r", encoding="utf-8") as f:
#     hits = [l.strip() for l in f if needle.lower() in l.lower()]
# print(hits)  # ['Ala ma kota', 'Kot lubi mleko']
#================================================================================================================
# 6) Zastąp słowo i zapisz do nowego pliku
# Cel: odczyt + zapis, tryb "w".

# src = r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst.txt"
# dst = r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst_rewrite.txt"
#
# with open(src, "r", encoding="utf-8") as f_in, open(dst, "w", encoding="utf-8") as f_out:
#     for line in f_in:
#         f_out.write(line.replace("Kot", "Pies").replace("kota", "psa"))

#================================================================================================================
# 7) Dopisz linię na końcu pliku
# Cel: tryb "a" (append).

# with open(r"C:\Users\lmala\OneDrive\Pulpit\korepetycje\pliki\29.10.25\tekst.txt", "a", encoding="utf-8") as f:
#     f.write("\nDopisany wiersz na końcu")
