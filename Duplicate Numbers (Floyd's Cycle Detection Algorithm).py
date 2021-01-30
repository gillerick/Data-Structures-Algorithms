def findDuplicate(arr):
    memo = {}
    for i in arr:
        memo[i] = 0

    for i in arr:
        memo[i] += 1
    return memo


print(findDuplicate([1, 5, 6, 7, 8, 1, 9]))
