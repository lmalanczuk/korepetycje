with open("tekst.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

# funkcja max z kluczem długości
longest = max(words, key=len)
print("Najdłuższe słowo w pliku:", longest)
