def fizzBuzz(n):
    i = 1
    buzzArray = []
    while i <= n:
        if (i % 3 == 0 and i % 5 == 0):
            buzzArray.append("FizzBuzz")

        elif (i % 3 == 0):
            buzzArray.append("Fizz")

        elif (i % 5 == 0):
            buzzArray.append("Buzz")
        else:
            buzzArray.append(str(i))
        i += 1
    print(buzzArray)