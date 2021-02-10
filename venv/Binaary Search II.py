def binary_search(array, item):
    low = 0
    high = len(array) - 1
    found = False
    count = 0
    while low <= high and not found:
        mid = (low + high) // 2
        if array[mid] == item:
            found = True
        else:
            if array[mid] > item:
                high = mid - 1
            else:
                low = mid + 1
        count += 1
    if found:
        print(f"{item} has been found  after {count} iterations.")
    else:
        print(f"{item} has not been found after {count} iterations.")


arr = [1, 3, 5,  6, 7, 9, 10, 23, 45, 54, 89, 100, 109]
x = 100
binary_search(arr, x)
