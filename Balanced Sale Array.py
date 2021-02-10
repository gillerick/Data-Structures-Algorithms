def balancedSales(sales):
    sum_left = 0
    sum_right = 0
    for i in range(1, len(sales)):
        sum_left = sum((sales[:i]))
        sum_right = sum((sales[i+1:]))
        if sum_left == sum_right:
            return i
        else:
            pass



print(balancedSales([1, 2, 3, 4, 6]))
