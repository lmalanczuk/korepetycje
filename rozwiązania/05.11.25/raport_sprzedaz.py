# 8_raport_sprzedaz.py
import csv

def to_float(x: str) -> float:
    return float(x.replace(",", "."))

def to_int(x: str) -> int:
    return int(x)

def main():
    with open("sprzedaz.csv", "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        rows = list(reader)

    wynik = []
    for r in rows:
        produkt = r["produkt"]
        cena = to_float(r["cena"])
        ilosc = to_int(r["ilosc"])
        wartosc = int(cena * ilosc) if (cena * ilosc).is_integer() else cena * ilosc
        wynik.append({"produkt": produkt, "wartosc": wartosc})

    with open("raport.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["produkt", "wartosc"], delimiter=";")
        writer.writeheader()
        writer.writerows(wynik)

if __name__ == "__main__":
    main()
