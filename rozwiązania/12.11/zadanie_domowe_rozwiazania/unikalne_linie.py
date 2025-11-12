# 4_unikatowe_linie.py
# Czyta "powtorzenia.txt", zapisuje unikalne linie (pierwsze wystąpienie)
# do "unikatowe.txt" w oryginalnej kolejności.

def main():
    seen = set()
    unique_lines = []

    with open("powtorzenia.txt", "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)

    with open("unikatowe.txt", "w", encoding="utf-8", newline="") as out:
        for ln in unique_lines:
            out.write(ln + "\n")

if __name__ == "__main__":
    main()
