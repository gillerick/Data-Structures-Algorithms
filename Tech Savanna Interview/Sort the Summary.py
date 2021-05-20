def groupSort(array):
    memo = {}
    multiArray = []

    sortedArraySet = sorted(set(array), reverse=True)
    for item in array:
        memo[item] = 0

    for item in array:
        memo[item] += 1

    print(memo)

    numbers = []
    frequencies = []

    for k, v in memo.items():
        numbers.append(k)
        frequencies.append(v)
        for num, freq in zip(numbers, frequencies):
            if next(numbers) == num:
                multiArray.insert(sortedArraySet.index(k-1), [k, v])
            else:
                multiArray.insert(sortedArraySet.index(k), [k, v])

    return multiArray


if __name__ == "__main__":
    array = [3, 3, 1, 1, 2]
    print(groupSort(array))


