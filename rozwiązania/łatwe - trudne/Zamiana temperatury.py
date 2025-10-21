temperatura_C = float(input("Podaj temperaturę w stopniach celsjusza: "))

temperatura_F = temperatura_C * 9/5 + 32
# round() to funkcja do zaokrąglania do najbliższego inta.
# można też jej użyć do zaokrąglania do x liczb po przecinku: round(liczba, x)
print(f"Temperatura w Fahrenheitach: {round(temperatura_F)}")