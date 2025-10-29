with open("temperatury.txt", "r", encoding="utf-8") as f:
    temps = [float(line.strip()) for line in f if line.strip()]

with open("ujemne.txt", "w", encoding="utf-8") as out:
    for t in temps:
        if t < 0:
            out.write(f"{t}\n")

print("Ujemne temperatury zapisano w pliku ujemne.txt.")
