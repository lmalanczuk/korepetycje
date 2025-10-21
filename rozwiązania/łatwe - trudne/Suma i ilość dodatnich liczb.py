lista = []
sum = 0
while True:
    y = int(input("Podaj liczbę dodatnią: "))
    lista.append(y)
    if y == 0:
        for i in lista:
            sum +=i
        break
print(f"Suma: {sum}")

