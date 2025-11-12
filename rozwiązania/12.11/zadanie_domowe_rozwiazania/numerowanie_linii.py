# 2_numerowanie_linii.py
# Dodaje numer linii na początku każdej linii z "wiersze.txt"
# i zapisuje do "ponumerowane.txt" w formacie: "1: treść"

def main():
    with open("wiersze.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("ponumerowane.txt", "w", encoding="utf-8", newline="") as out:
        for idx, line in enumerate(lines, start=1):
            out.write(f"{idx}: {line.rstrip()}\n")

if __name__ == "__main__":
    main()
