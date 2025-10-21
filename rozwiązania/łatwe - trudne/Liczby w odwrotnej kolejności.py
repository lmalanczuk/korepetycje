liczba = int(input("Podaj liczbę: "))

liczba_string = str(liczba)

# zapis [::-1] to slicing. struktura: [pierwsza_wartość:ostatnia_wartość:krok] -> tak samo jak w for i in range[0,100,1]
print(liczba_string[::-1])