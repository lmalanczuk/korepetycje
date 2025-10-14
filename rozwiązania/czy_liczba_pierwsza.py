def czy_pierwsza_simple(n):
    if n < 2:
        return False
    # próbujemy dzielić przez wszystkie liczby 2..n-1
    for d in range(2, n):
        if n % d == 0:  # reszta 0 -> d dzieli n, więc n nie jest pierwsza
            return False
    return True

print(czy_pierwsza_simple(2))
print(czy_pierwsza_simple(15))

def czy_pierwsza(n: int) -> bool:
    if n < 2:
        return False
    # dzielenie próbne tylko do pierwiastka z n (każdy większy dzielnik ma parę mniejszą)
    # int(n ** 0.5) -> część całkowita z pierwiastka (zob. ** to potęgowanie)
    limit = int(n ** 0.5)
    for d in range(2, limit + 1):
        if n % d == 0:
            return False
    return True

# Różnice:
# - Wersja sqrt jest asymptotycznie szybsza (O(√n) vs O(n)).
# - Dla dużych n to ma bardzo duże znaczenie.

