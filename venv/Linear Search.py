def linear_search(array, item):
    found = False
    if len(array) < 1:
        return print("List too short!")
    else:
        while not found:
            for i in range(len(array)):
                if array[i] == item:
                    found = True

                    return print(f"{item} has been found at position {i+1}")


x = [2, 4, 5, 7, 23, 12, 23, 20]
y = 5
linear_search(x, y)
