def suma_do_n_loop(n):
    # Zakładamy n >= 0
    s = 0
    # range(n + 1) -> 0..n
    for i in range(n + 1):
        s += i  # += dodaje i do bieżącej sumy
    return s

print(suma_do_n_loop(5))

def suma_do_n(n: int) -> int:
    # Wzór arytmetyczny: 0+1+...+n = n*(n+1)//2
    # // -> dzielenie całkowite (wynik bez części ułamkowej)
    return n * (n + 1) // 2

# Różnice:
# - Pętla: dydaktyczna, działa dla każdego n (także gdy chcemy logikę per element).
# - Wzór: O(1) czas i pamięć — najlepszy wydajnościowo i najprostszy w zapisie.