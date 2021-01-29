def median(arr):
    l = len(arr)
    if l % 2 == 0:
        return sum(map(int, arr[int(l/2-1):int(l/2+1)]))/2
    else:
        return arr[l//2]


print(median([3, 4, 5, 6, 7]))
print(median([3, 4, 5, 6, 7, 9]))
