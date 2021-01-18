def binary_search(array, x):
    if len(array) < 1:
        print("Array size too small")
    low = 0
    high = len(array) - 1
    found = False
    count = 0
    while high >= low and found is False:
        mid = (low + high) // 2

        if array[mid] == x:
            found = True
            # print(f"{x} found.")

        else:
            if x > array[mid]:
                low = mid + 1
                count += 1
            else:
                high = mid - 1
                count += 1

    if found:
        print(f"{x} found after {count} iterations.")
    else:
        print("Item not in array")


a = [3, 5, 6, 7, 8, 9, 10, 12, 15, 17, 18]
_x = 8


binary_search(a, _x)
