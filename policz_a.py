def policz_a_loop(s):
    count = 0
    for ch in s:
        if ch == 'a':
            count += 1
    return count

print(policz_a_loop("alabama"))
print(policz_a_loop("python"))

def policz_a(s: str) -> int:
    # s.count('a') -> wbudowana metoda stringa licząca wystąpienia podciągu 'a'
    # Szybka i czytelna; implementacyjnie wydajniejsza niż ręczna pętla w Pythonie.
    return s.count('a')

# Różnice:
# - .count jest krótsze i zwykle szybsze (część w C), pętla jest "manualna" i dydaktyczna.
