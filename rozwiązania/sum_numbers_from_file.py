def sum_numbers_from_file():
    with open("numbers.txt", "r") as f:
        numbers = f.readlines()
        numbers_added = 0

        for i in numbers:
            numbers_added += int(i)

    print(numbers_added)


sum_numbers_from_file()
