import sys
n = 50
arr = []

for i in range(n):
    a = len(arr)
    b = sys.getsizeof(arr)
    print(f"Length of array: {a:3d}. Size of array {b:4d}")

    arr.append(n)