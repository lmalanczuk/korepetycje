def najdluzsze_slowo_simple(words):
    if not words:
        return ""
    longest = words[0]
    for w in words[1:]:
        if len(w) > len(longest):  # len(x) -> długość napisu/listy/etc.
            longest = w
    return longest

print(najdluzsze_slowo_simple(["ala", "makarena", "kot"]))
print(najdluzsze_slowo_simple([]))

from typing import List

def najdluzsze_slowo(words: List[str]) -> str:
    if not words:
        return ""
    # max(iterowalny, key=func) -> wybiera element o największej wartości klucza
    # Tu kluczem jest długość; Pythonowy, czytelny idiom.
    # "Stable enough": zwróci pierwsze o max długości (bo max nie przestawia elementów).
    return max(words, key=len)

# Różnice:
# - Ręczna pętla jest dydaktyczna i jawna.
# - max(key=len) jest krótsze, czytelniejsze i bardziej idiomatyczne w Pythonie.
