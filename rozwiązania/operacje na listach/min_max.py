def min_max_simple(nums):
    if not nums:
        return None, None
    mn = mx = nums[0]
    #nums[1:] oznacza, że zaczynamy od indeksu 1 i idziemy do końca listy
    for x in nums[1:]:
        # min(a,b), max(a,b) -> zwraca odpowiednio mniejszą/większą z wartości
        mn = x if x < mn else mn
        mx = x if x > mx else mx
    return mn, mx

print(min_max_simple([5, 2, 9, -1, 6]))
