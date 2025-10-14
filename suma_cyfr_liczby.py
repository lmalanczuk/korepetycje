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
assert suma_cyfr(451) == 10
assert suma_cyfr(0) == 0  # pętla się nie wykona, s=0 pozostaje