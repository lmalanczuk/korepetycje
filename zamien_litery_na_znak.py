def leet_replace_simple(s):
    # s.replace(x, y) -> zwraca nowy string z zamianą wszystkich x na y
    # Uwaga: łańcuchowe replace działa poprawnie, bo mapujemy różne znaki (nie wchodzą sobie w drogę)
    s = s.replace('a', '@')
    s = s.replace('e', '3')
    s = s.replace('o', '0')
    return s

print(leet_replace_simple("alabama"))
print(leet_replace_simple("omelet"))

def leet_replace(s: str) -> str:
    # str.maketrans(dict) -> buduje tablicę translacji znaków (tu: a,e,o)
    trans = str.maketrans({'a': '@', 'e': '3', 'o': '0'})
    # s.translate(tablica) -> zwraca napis po jednoprzebiegowej translacji znaków
    return s.translate(trans)

# Zalety translate:
# - jeden przebieg po stringu (zwykle szybszy niż kilka .replace)
# - łatwo dodać więcej zamian w jednym miejscu
