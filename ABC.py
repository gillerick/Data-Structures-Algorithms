from itertools import combinations


def abc(arr):
    C = []
    for num in range(len(arr) + 1):
        c_object = combinations(arr, num)
        c_list = list(c_object)
        C += c_list
    return print(C)


if __name__ == "__main__":
    print(abc([3, 5, 6]))
