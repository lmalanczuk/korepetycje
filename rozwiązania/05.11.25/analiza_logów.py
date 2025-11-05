# 10_analiza_logow.py
def main():
    # Kolejność pierwszych LOGOWAŃ zachowamy w liście; set do szybkiej kontroli
    kolejnosc = []
    widziani = set()

    with open("logi.txt", "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            # oczekiwany format: "YYYY-MM-DD HH:MM:SS AKCJA user"
            # bierzemy tylko pierwsze LOGI(N) dla danego usera
            czesci = s.split()
            if len(czesci) < 4:
                continue
            akcja = czesci[2].upper()
            user = czesci[3]
            if akcja == "LOGIN" and user not in widziani:
                widziani.add(user)
                kolejnosc.append(user)

    with open("statystyka.txt", "w", encoding="utf-8") as out:
        out.write(f"Liczba różnych zalogowanych użytkowników: {len(kolejnosc)}\n")
        out.write("Kolejność pierwszych logowań:\n")
        out.write("\n".join(kolejnosc))

if __name__ == "__main__":
    main()
