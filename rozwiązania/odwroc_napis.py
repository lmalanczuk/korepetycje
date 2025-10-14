def reverse_loop(s):
    out = ""
    # range(len-1, -1, -1) -> idziemy od ostatniego indeksu do 0
    for i in range(len(s) - 1, -1, -1):
        out += s[i]  # konkatenacja stringów; prosta, ale mniej wydajna przy bardzo długich napisach
    return out

print(reverse_loop("python"))
print(reverse_loop(""))

def reverse(s: str) -> str:
    # s[::-1] -> "slicing" z krokiem -1: bierze cały napis od końca do początku
    # Bardzo krótki i czytelny idiom w Pythonie.
    return s[::-1]

# Alternatywa: ''.join(reversed(s)) -> też działa, czasem lepsza, gdy chcemy iterator reversed()
