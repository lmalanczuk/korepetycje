def policz_parzyste_nieparzyste_simple(nums):
    parz = 0
    nieparz = 0
    for x in nums:
        # x % 2 == 0 -> liczba parzysta
        if x % 2 == 0:
            parz += 1  # += -> zwiększ o 1
        else:
            nieparz += 1
    # zwracamy krotkę (para wartości)
    return (parz, nieparz)

print(policz_parzyste_nieparzyste_simple([1, 2, 3, 4, 5]))

from typing import Iterable, Tuple

def policz_parzyste_nieparzyste(nums: Iterable[int]) -> Tuple[int, int]:
    # Iterable[int] -> funkcja przyjmie dowolną kolekcję liczb (lista, krotka, generator)
    # Tuple[int, int] -> zwracamy parę (parzyste, nieparzyste)
    parz: int = 0
    nieparz: int = 0
    for x in nums:
        if x % 2 == 0:  # % -> reszta z dzielenia; dla 2 sprawdza parzystość
            parz += 1
        else:
            nieparz += 1
    return parz, nieparz  # Python pozwala zwrócić krotkę bez nawiasów

# Różnice i zalety:
# - Typy pomagają IDE/static checkerom (mniej błędów, łatwiej utrzymać kod).
# - Iterable zamiast listy: funkcja działa też na generatorach (strumienie, duże zbiory).
