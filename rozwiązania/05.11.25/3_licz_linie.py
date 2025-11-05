# 3_licz_linie.py
def main():
    with open("dane.txt", "r", encoding="utf-8") as f:
        liczba = sum(1 for _ in f)
    print(f"Liczba linii: {liczba}")

if __name__ == "__main__":
    main()
