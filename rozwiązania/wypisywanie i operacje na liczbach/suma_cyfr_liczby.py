def suma_cyfr(n):
    # abs(x) -> zwraca wartość bezwzględną; tu "ściągamy" minus ze znakowanych liczb
    n = abs(n)

    s = 0
    while n > 0:
        # n % 10 -> reszta z dzielenia przez 10, czyli "ostatnia cyfra" liczby n
        s += n % 10  # operator += zwiększa zmienną z lewej o wartość z prawej (s = s + ...)
        # n //= 10 -> dzielenie całkowite; "obcinamy" ostatnią cyfrę (np. 451 // 10 = 45)
        n //= 10
    return s

# przykłady
print(suma_cyfr(451))
print(suma_cyfr(0))

# zapis (n: int) -> int to tzw. adnotacje typów. Pokazujemy jaki typ chcemy przyjąć i jaki tym chcemy zwrócić.
def suma_cyfr_num(n: int) -> int:
    n = abs(n)  # patrz komentarz wyżej: wartość bezwzględna
    s: int = 0
    while n:
        s += n % 10   # % -> reszta z dzielenia
        n //= 10      # // -> dzielenie całkowite
    return s

#ALTERNATYWA -> z użyciem str
# def suma_cyfr_str(n: int) -> int:
#     # Alternatywa: konwersja na napis i sumowanie cyfr przez mapowanie na int.
#     # To bywa czytelniejsze dla początkujących, ale ma narzut konwersji liczba->string->liczby.
#     return sum(int(ch) for ch in str(abs(n)))

# różnice: wersja numeryczna uczy "operacji na cyfrach" (algorytmiczna),
# wersja stringowa jest krótsza i bardzo czytelna dla małych skryptów.