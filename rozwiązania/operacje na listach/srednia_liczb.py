def srednia_loop(nums):
    if not nums:        # pusty zbiór -> zapobiegamy dzieleniu przez zero
        return 0.0
    s = 0
    count = 0
    for x in nums:
        s += x
        count += 1
    # / -> dzielenie zmiennoprzecinkowe; wynik float nawet, jeśli s i count są int
    return s / count


print(abs(srednia_loop([4, 6, 8])))

