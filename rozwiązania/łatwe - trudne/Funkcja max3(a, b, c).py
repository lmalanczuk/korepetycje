def max3(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return "Podałeś 2 lub więcej takich samych liczb"


print(max3(2,7,7))