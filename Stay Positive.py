def minStart(arr):
    min_start = 0
    cache = {}
    # Test base case where there all integers are positive
    if all([x > 0 for x in arr]):
        return min_start
    else:
        for item in arr:
            cache[item] = arr.index(item)
        # Store the negative numbers in a dict
        min_negative = min([y for y in arr if y < 0])
        index_of_min_negative = cache[min_negative]
        # Searching through the negative number in the dictionary
        sum_before = sum(arr[:index_of_min_negative])
        min_start = abs(min_negative) - sum_before + 1
        return min_start


print(minStart([3, -6, 5, 1]))
print(minStart([-4, 3, 2, 1]))

