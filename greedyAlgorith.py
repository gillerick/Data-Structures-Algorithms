denominations = [100, 500, 50, 200, 1000, 20, 10, 5, 1]


def findMin(V):
    size = len(denominations)
    result = []
    i = size - 1
    while (i >= 0):
        while (V >= denominations[i]):
            V -= denominations[i]
            result.append(denominations[i])

        i -= 1

    # Print result
    for i in range(len(result)):
        print(result[i], end=" ")


# Driver Code
if __name__ == '__main__':
    findMin(567)
