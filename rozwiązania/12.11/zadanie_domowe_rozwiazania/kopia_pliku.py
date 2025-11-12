# 1_kopia_pliku.py
# Wczytuje "oryginal.txt" i zapisuje do "kopia.txt"

def main():
    with open("oryginal.txt", "r", encoding="utf-8") as src:
        content = src.read()
    with open("kopia.txt", "w", encoding="utf-8", newline="") as dst:
        dst.write(content)

if __name__ == "__main__":
    main()