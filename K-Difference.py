"""
Given an array of distinct integers and a target value, determine the number of distinct pairs in integers

"""


def k_difference(arr):
    C = []
    for i in range(1, len(arr)):
        try:
            C += [arr[i-1], arr[i], arr[i+1]]
        except IndexError:
            pass
    print(C)


if __name__ == "__main__":
    print(k_difference([2, 4, 5, 8]))
