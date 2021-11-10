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


numbers = [45, 56, 34, 48][0:3]
# start:stop (exclusive)
# print(numbers[0:3])
# print(numbers[:3])
# print("\n")
# print(numbers[1:4])
# print(numbers[1:])
#
# print(numbers)


array = list(map(int, input().split(' ')))
# n = input().split(' ')
# n_map = map(int, n)
# print(n_map)
# print(type(n_map))

# first = n[0]
# print(first)
# print(type(first))
# Type casting
first = array[0]
print(array)
print(type(first))
