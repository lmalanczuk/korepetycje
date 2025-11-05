# 2_bez_pustych_linii.py
def main():
    with open("tekst.txt", "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:  # pomijamy puste
                print(s)

if __name__ == "__main__":
    main()
