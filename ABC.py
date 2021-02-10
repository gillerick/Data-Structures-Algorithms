from itertools import combinations

def ABC(arr):
    C = []
    for num in range(len(arr) + 1):
        c_object = combinations(arr, num)
        c_list = list(c_object)
        C += c_list
    return print(C)

ABC([3, 5, 6])
