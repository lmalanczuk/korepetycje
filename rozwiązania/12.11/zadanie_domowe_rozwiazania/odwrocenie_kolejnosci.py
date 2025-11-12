# 3_odwrocenie_kolejnosci.py
# Czyta "teksty.txt" i zapisuje linie w odwrotnej kolejności do "odwrocone.txt"

def main():
    with open("teksty.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [ln.rstrip("\n") for ln in lines]
    lines.reverse()

    with open("odwrocone.txt", "w", encoding="utf-8", newline="") as out:
        out.write("\n".join(lines))
        out.write("\n")  # opcjonalnie: końcowy newline

if __name__ == "__main__":
    main()
