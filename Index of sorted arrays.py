def reduced_array():
    a = int(input())
    for i in range(1, a):
        array_size = int(input())
        # takes the array and split to comma separated items
        array = list(map(int, input().split(' ')))[:array_size]
        # sort the array
        sortedArray = sorted(array)

        # an empty dictionary that stores the key and values of the sorted array
        ranks = {}

        result = []
        # creates the item and value key
        for rank, item in enumerate(sortedArray):
            ranks[rank] = item

        # reference the first array and find their indexes
        for rank, item in ranks.items():
            result.insert(array.index(item), rank)

        return result


# Output the variable to STDOUT

if __name__ =="main_":
    print(reduced_array())
