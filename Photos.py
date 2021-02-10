from itertools import combinations
# from typing import List

def combine(arr):
    print(list(x for l in range(2, len(arr)+1) for x in combinations(arr, l) if 1 in x))


print(combine([1, 2, 3]))
