# 1_odczyt.py
def main():
    with open("wiersz.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.rstrip("\n"))

if __name__ == "__main__":
    main()
