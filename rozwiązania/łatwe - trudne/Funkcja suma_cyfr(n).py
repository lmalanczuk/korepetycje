def suma_cyfr(n):
    liczba_string = str(n)
    suma = 0
    for i in liczba_string:
        suma += int(i)
    return suma


print(suma_cyfr(1234))