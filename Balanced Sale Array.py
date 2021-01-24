def balancedSales(arr):
    sum_left = 0
    sum_right = 0
    for i in range(1, len(arr)):
        sum_left = sum((arr[:i]))
        sum_right = sum((arr[i+1:]))
        if sum_left == sum_right:
            return i
        else:
            pass



print(balancedSales([1, 2, 3, 4, 6]))
