# 5_temperatury_ujemne.py
def main():
    ujemne = []
    with open("temperatury.txt", "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            t = float(s.replace(",", "."))  # dopuszczamy przecinek
            if t < 0:
                ujemne.append(s)

    with open("ujemne.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(ujemne))

if __name__ == "__main__":
    main()
