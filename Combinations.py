# from itertools import combinations

even = [2, 4]
odd = [1, 3, 5]

arr = [1, 2, 4]
photos = []
count = 0


def combinations(lst, n):
    if n == 0:
        return [[]]

    l = []
    C = []
    for i in range(2, len(lst)+1):
        m = lst[i]
        if lst[i] % 2 == 0:
            remainder = [e for e in lst[i + 1:] if e % 2 != 0]
            for p in combinations(remainder, n-1):
                l.append([m]+p)

        else:
            remainder = [o for o in lst[i + 1:] if o % 2 == 0]
            for p in combinations(remainder, n-1):
                l.append([m]+p)
        return l



def helper():
    for j in range(len(odd)):
        arr = []
        arr.extend([*[x for x in even if x < odd[j]], odd[j]])
        print(combinations(arr, len(arr)))

    for k in range(len(even)):
        arr = []
        arr.extend([*[y for y in odd if y < even[k]], even[k]])
        print(arr)


print(helper())
