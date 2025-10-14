# definicja funkcji -> funkcja to taki "zbiór" instrukcji, które chcemy wykonać
def temp_conversion():
    celsius = float(input("Podaj temperaturę w stopniach celsjusza: "))

    fahrenheit = (celsius * 9 / 5) + 32

    print(fahrenheit)


temp_conversion()


def temp_conversion_reverse():
    fahrenheit = float(input("Podaj temperaturę w stopniach fahrenheita: "))
    celsius = (fahrenheit - 32) * 5 / 9

    print(celsius)


temp_conversion_reverse()
