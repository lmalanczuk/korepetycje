import random

losowa_liczba = random.randint(0,100)

while True:
    liczba = int(input("Zgadnij liczbę z zakresu 0 - 100: "))
    if liczba == losowa_liczba:
        print("Zgadłeś!")
        break
    elif liczba > losowa_liczba:
        print("Za dużo")
    else:
        print("Za mało")