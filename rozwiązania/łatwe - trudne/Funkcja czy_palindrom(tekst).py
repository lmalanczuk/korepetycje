def czy_palindrom(tekst):
    if tekst == tekst[::-1]:
        return True
    else:
        return False


print(czy_palindrom("python"))
print(czy_palindrom("kajak"))