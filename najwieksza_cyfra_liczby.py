def najwieksza_cyfra(n):
    n = abs(n)  # usuń znak
    if n == 0:
        return 0
    m = 0
    while n:
        # n % 10 -> ostatnia cyfra
        cyfra = n % 10
        # max(a, b) -> zwraca większą z wartości a i b
        m = max(m, cyfra)
        # n //= 10 -> zaokrąglenie do najbliższej pełnej liczby
        n //= 10
    return m

print(najwieksza_cyfra(9473))
print(najwieksza_cyfra(10020))


def najwieksza_cyfra_num(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    m: int = 0
    while n:
        m = max(m, n % 10)  # % -> ostatnia cyfra
        n //= 10            # // -> ucięcie ostatniej cyfry
    return m

# def najwieksza_cyfra_str(n: int) -> int:
#     # max(iterowalny) na stringu -> zwróci największy znak według porządku leksykalnego,
#     # ale dla cyfr '0'..'9' to jest zgodne z ich wartościami, więc konwertujemy na int.
#     return max(int(ch) for ch in str(abs(n)))

# Różnice: wersja numeryczna – typowo "algorytmiczna".
# Wersja "stringowa" – krótsza, ale opiera się na konwersji do napisu.