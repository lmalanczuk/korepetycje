# 7_licz_wystapienia_python.py
import re

def main():
    with open("tekst.txt", "r", encoding="utf-8") as f:
        tekst = f.read()
    # \b – granice słowa; ignorujemy wielkość liter
    liczba = len(re.findall(r"\bpython\b", tekst, flags=re.IGNORECASE))
    print('Liczba wystąpień słowa "Python":', liczba)

if __name__ == "__main__":
    main()
