def reduced_form():
    test_cases = int(input())
    for i in range(test_cases):
        reduced_forms = {}
        # Initialize array to store element positions
        positions = []
        # Take in size of array
        array_size = int(input())
        # Take in array elements
        array_elements = input().split()
        # Converting array elements to list & slicing it based on no of test cases
        array_elements = list(map(int, array_elements))[:array_size]
        # Sorting the resultant array
        ordered_arrays = sorted(array_elements)
        for position, element in enumerate(ordered_arrays):
            reduced_forms[position] = element
        for position, element in reduced_forms.items():
            positions.insert(array_elements.index(element), position)
        print(positions)


if __name__ == "__main__":
    print(reduced_form())


numbers = [1, 2, 3, 6, 8, 9, 6, 67, 34]






# founders = {'Apple': 'Steve Jobs', 'Microsoft': 'Bill Gates'}
# founders['Oracle'] = 'Larry Ellison'
# print(founders)



# numbers = [45, 67, 5]
# numbers.append(78)
# numbers.append(56)
# numbers.insert(2, 75)
# # print(numbers.index(5))
# print(numbers[:3])
