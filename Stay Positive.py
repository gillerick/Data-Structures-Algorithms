"""
There is a given array of integers. Start with some value x, and add each of the array elements to it consecutively.
That is, calculate a running sum of x plus each of the array elements. Determine the minimum value of x such that the
running sum is always at least 1 even at the outset. The value of x can never be less than 1.

"""

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

